import 'package:flutter/material.dart';

class RoleChip extends StatelessWidget {
  final String role;

  const RoleChip(this.role, {super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 4),
      decoration: BoxDecoration(
        color: Colors.blueGrey[700],
        borderRadius: BorderRadius.circular(4),
      ),
      child: Text(role, style: const TextStyle(color: Colors.white70, fontSize: 12)),
    );
  }
}
