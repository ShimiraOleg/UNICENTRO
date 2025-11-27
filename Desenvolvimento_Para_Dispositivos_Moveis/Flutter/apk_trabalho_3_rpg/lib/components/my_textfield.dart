import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class MyTextfield extends StatefulWidget {
  final TextEditingController controller;
  final String hintText;
  final bool obscureText;
  final TextInputType? keyboardType;
  const MyTextfield({
    super.key,
    required this.controller,
    required this.hintText,
    required this.obscureText,
    this.keyboardType,
  });

  @override
  State<MyTextfield> createState() => _MyTextfieldState();
}

class _MyTextfieldState extends State<MyTextfield> {
  late bool _isObscured;
  late TextInputType? _keyboard;

  @override
  void initState() {
    super.initState();
    _isObscured = widget.obscureText;
    _keyboard = widget.keyboardType;
  }

  @override
  Widget build(BuildContext context) {
    final TextStyle fontStyle = GoogleFonts.roboto(color: Colors.brown[900]);

    return Padding(
      padding: const EdgeInsets.symmetric(horizontal: 25.0),
      child: TextField(
        controller: widget.controller,
        obscureText: _isObscured,
        keyboardType: _keyboard,
        style: fontStyle,
        cursorColor: Colors.brown[900],
        decoration: InputDecoration(
          enabledBorder: const OutlineInputBorder(borderSide: BorderSide(color: Colors.brown)),
          focusedBorder: OutlineInputBorder(
            borderSide: BorderSide(color: Colors.brown.shade900, width: 2),
          ),
          fillColor: const Color(0x80FFFFFF),
          filled: true,
          hintText: widget.hintText,
          hintStyle: fontStyle.copyWith(color: Colors.brown.withValues(alpha: 0.5)),
          suffixIcon: widget.obscureText
              ? IconButton(
                  icon: Icon(
                    _isObscured ? Icons.visibility_off : Icons.visibility,
                    color: Colors.brown,
                  ),
                  onPressed: () {
                    setState(() {
                      _isObscured = !_isObscured;
                    });
                  },
                )
              : null,
        ),
      ),
    );
  }
}
