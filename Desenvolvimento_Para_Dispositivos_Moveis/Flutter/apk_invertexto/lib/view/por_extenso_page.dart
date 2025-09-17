import 'dart:convert';
import 'package:apk_invertexto/service/invertexto_service.dart';
import 'package:flutter/material.dart';

class PorExtensoPage extends StatefulWidget {
  const PorExtensoPage({super.key});

  @override
  State<PorExtensoPage> createState() => _PorExtensoPageState();
}

class _PorExtensoPageState extends State<PorExtensoPage> {
  String? campo;
  String? moeda;
  String? resultado;
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
        padding: EdgeInsets.all(10.0),
        child: Column(
          children: <Widget>[
            TextField(
              decoration: InputDecoration(
                labelText: 'Digite um número',
                labelStyle: TextStyle(color: Colors.white),
                border: OutlineInputBorder(),
              ),
              keyboardType: TextInputType.number,
              style: TextStyle(color: Colors.white, fontSize: 18),
              onSubmitted: (value) {
                setState(() {
                  campo = value;
                });
              },
            ),
            SizedBox(height: 30),
            Text(
              "Selecione uma Moeda: ",
              style: TextStyle(color: Colors.white, fontSize: 18),
            ),
            DropdownButton(
              value: moeda,
              style: TextStyle(color: Colors.white, fontSize: 18),
              dropdownColor: Colors.black,
              items: [
                DropdownMenuItem(value: "BRL", child: Text("Real (BRL)")),
                DropdownMenuItem(value: "USD", child: Text("Dólar (USD)")),
                DropdownMenuItem(value: "EUR", child: Text("Euro (EUR)")),
                DropdownMenuItem(value: "GBP", child: Text("Libra Esterlina (GBP)")),
                DropdownMenuItem(value: "JPY", child: Text("Iene (JPY)")),
                DropdownMenuItem(value: "ARS", child: Text("Peso Argentino (ARS)")),
                DropdownMenuItem(value: "MXN", child: Text("Peso Mexicano (MXN)")),
                DropdownMenuItem(value: "UYU", child: Text("Peso Uruguaio (UYU)")),
                DropdownMenuItem(value: "PYG", child: Text("Guarani (PYG)")),
                DropdownMenuItem(value: "BOB", child: Text("Boliviano (BOB)")),
                DropdownMenuItem(value: "CLP", child: Text("Peso Chileno (CLP)")),
                DropdownMenuItem(value: "COP", child: Text("Peso Colombiano (COP)")),
                DropdownMenuItem(value: "CUP", child: Text("Peso Cubano (CUP)")),
              ],
              onChanged: (value) {
                setState(() {
                  moeda = value;
                });
              },
            ),
            SizedBox(height: 30),
            Expanded(
              child: FutureBuilder(
                future: apiService.convertePorExtenso(campo, moeda),
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
    return Padding(
      padding: EdgeInsets.only(top: 10.0),
      child: Text(
        snapshot.data['text'] ?? '',
        style: TextStyle(color: Colors.white, fontSize: 18),
        softWrap: true,
      ),
    );
  }

  Widget exibeErrorMessage(String error) {
    int inicioErro = error.lastIndexOf(': ') + 2;
    String erroJson = error.substring(inicioErro);
    Map<String, dynamic> displayError = jsonDecode(erroJson);
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Text(
          displayError['message']!,
          textAlign: TextAlign.center,
          style: const TextStyle(
            color: Colors.white,
            fontSize: 16,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
    );
  }
}
