import 'package:flutter/material.dart';

class ConversorMoedaPage extends StatefulWidget {
  const ConversorMoedaPage({super.key});

  @override
  State<ConversorMoedaPage> createState() => _ConversorMoedaPageState();
}

class _ConversorMoedaPageState extends State<ConversorMoedaPage> {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.black,
        title: Row(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Image.asset(
              'assets/imgs/logo.png',
              fit: BoxFit.contain,
              height: 40,
            ),
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
    );
  }
}
