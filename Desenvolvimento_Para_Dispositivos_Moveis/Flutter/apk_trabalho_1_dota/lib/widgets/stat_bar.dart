import 'package:flutter/material.dart';

class StatBar extends StatelessWidget {
  final Color barColor;
  final String baseValue;
  final String gainValue;

  const StatBar({
    super.key,
    required this.barColor,
    required this.baseValue,
    required this.gainValue,
  });

  @override
  Widget build(BuildContext context) {
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
              style: const TextStyle(
                color: Colors.white,
                fontSize: 20,
                fontWeight: FontWeight.bold,
                shadows: [Shadow(blurRadius: 2.0)],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
