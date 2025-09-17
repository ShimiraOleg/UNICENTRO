import 'dart:convert';
import 'package:apk_invertexto/service/invertexto_service.dart';
import 'package:flutter/material.dart';

class ConversorMoedaPage extends StatefulWidget {
  const ConversorMoedaPage({super.key});

  @override
  State<ConversorMoedaPage> createState() => _ConversorMoedaPageState();
}

class _ConversorMoedaPageState extends State<ConversorMoedaPage> {
  String? moeda1;
  String? moeda2;
  final apiService = InvertextoService();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.black,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset('assets/imgs/logo.png', fit: BoxFit.contain, height: 40),
          ],
        ),
        centerTitle: true,
        leading: IconButton(
          onPressed: () {
            Navigator.pop(context);
          },
          icon: Icon(Icons.arrow_back, color: Colors.white),
        ),
      ),
      backgroundColor: Colors.black,
      body: Padding(
        padding: EdgeInsets.all(10),
        child: Column(
          children: <Widget>[
            DropdownButton(
              value: moeda1,
              style: TextStyle(color: Colors.white, fontSize: 18),
              dropdownColor: Colors.black,
              items: [
                DropdownMenuItem(value: "BRL", child: Text("BRL")),
                DropdownMenuItem(value: "USD", child: Text("USD")),
                DropdownMenuItem(value: "EUR", child: Text("EUR")),
                DropdownMenuItem(value: "GBP", child: Text("GBP")),
                DropdownMenuItem(value: "JPY", child: Text("JPY")),
                DropdownMenuItem(value: "ARS", child: Text("ARS")),
                DropdownMenuItem(value: "MXN", child: Text("MXN")),
                DropdownMenuItem(value: "UYU", child: Text("UYU")),
                DropdownMenuItem(value: "PYG", child: Text("PYG")),
                DropdownMenuItem(value: "BOB", child: Text("BOB")),
                DropdownMenuItem(value: "CLP", child: Text("CLP")),
                DropdownMenuItem(value: "COP", child: Text("COP")),
                DropdownMenuItem(value: "CUP", child: Text("CUP")),
              ],
              onChanged: (value) {
                setState(() {
                  moeda1 = value;
                });
              },
            ),
            SizedBox(height: 45),
            DropdownButton(
              value: moeda2,
              style: TextStyle(color: Colors.white, fontSize: 18),
              dropdownColor: Colors.black,
              items: [
                DropdownMenuItem(value: "BRL", child: Text("BRL")),
                DropdownMenuItem(value: "USD", child: Text("USD")),
                DropdownMenuItem(value: "EUR", child: Text("EUR")),
                DropdownMenuItem(value: "GBP", child: Text("GBP")),
                DropdownMenuItem(value: "JPY", child: Text("JPY")),
                DropdownMenuItem(value: "ARS", child: Text("ARS")),
                DropdownMenuItem(value: "MXN", child: Text("MXN")),
                DropdownMenuItem(value: "UYU", child: Text("UYU")),
                DropdownMenuItem(value: "PYG", child: Text("PYG")),
                DropdownMenuItem(value: "BOB", child: Text("BOB")),
                DropdownMenuItem(value: "CLP", child: Text("CLP")),
                DropdownMenuItem(value: "COP", child: Text("COP")),
                DropdownMenuItem(value: "CUP", child: Text("CUP")),
              ],
              onChanged: (value) {
                setState(() {
                  moeda2 = value;
                });
              },
            ),
            SizedBox(height: 30),
            Expanded(
              child: FutureBuilder(
                future: apiService.conversorMoeda(moeda1, moeda2),
                builder: (context, snapshot) {
                  switch (snapshot.connectionState) {
                    case ConnectionState.waiting:
                    case ConnectionState.none:
                      return Container(
                        width: 200,
                        height: 200,
                        alignment: Alignment.center,
                        child: CircularProgressIndicator(
                          valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
                          strokeWidth: 8.0,
                        ),
                      );
                    default:
                      if (snapshot.hasError) {
                        return exibeErrorMessage(snapshot.error.toString());
                      } else {
                        return exibeResultado(context, snapshot);
                      }
                  }
                },
              ),
            ),
          ],
        ),
      ),
    );
  }

  Widget exibeResultado(BuildContext context, AsyncSnapshot snapshot) {
    final resultado = snapshot.data["${moeda1}_$moeda2"];
    return Padding(
      padding: EdgeInsets.only(top: 10.0),
      child: Text(
        "1 $moeda1 equivale a ${resultado['price']} $moeda2",
        style: TextStyle(color: Colors.white, fontSize: 18),
        softWrap: true,
      ),
    );
  }

  Widget exibeErrorMessage(String error) {
    final displayError = error.replaceFirst("Exception: ", "");
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Text(
          'Ocorreu um erro:\n$displayError',
          textAlign: TextAlign.center,
          style: const TextStyle(
            color: Colors.redAccent,
            fontSize: 18,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
    );
  }
}
