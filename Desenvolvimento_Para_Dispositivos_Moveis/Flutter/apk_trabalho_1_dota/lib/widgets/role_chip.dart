import 'package:flutter/material.dart';

Widget roleChip(String role) {
  return Container(
    padding: EdgeInsets.symmetric(horizontal: 8, vertical: 4),
    decoration: BoxDecoration(
      color: Colors.blueGrey[700],
      borderRadius: BorderRadius.circular(4),
    ),
    child: Text(role, style: TextStyle(color: Colors.white70, fontSize: 12)),
  );
}
