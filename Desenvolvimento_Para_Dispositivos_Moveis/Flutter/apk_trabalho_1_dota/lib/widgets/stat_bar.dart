import 'package:flutter/material.dart';

Widget statBar(Color barColor, String baseValue, String gainValue) {
  return Container(
    color: barColor,
    padding: const EdgeInsets.symmetric(horizontal: 16.0, vertical: 8.0),
    child: Stack(
      children: [
        Center(
          child: Text(
            baseValue,
            style: const TextStyle(
              color: Colors.white,
              fontSize: 24,
              fontWeight: FontWeight.bold,
              shadows: [Shadow(blurRadius: 2.0)],
            ),
          ),
        ),
        Align(
          alignment: Alignment.centerRight,
          child: Text(
            "+ $gainValue",
            style: TextStyle(
              color: Colors.white,
              fontSize: 20,
              fontWeight: FontWeight.bold,
              shadows: const [Shadow(blurRadius: 2.0)],
            ),
          ),
        ),
      ],
    ),
  );
}
