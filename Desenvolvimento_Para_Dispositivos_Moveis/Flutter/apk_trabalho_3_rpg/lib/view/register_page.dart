import 'package:apk_trabalho_3_rpg/components/my_button.dart';
import 'package:apk_trabalho_3_rpg/components/my_textfield.dart';
import 'package:apk_trabalho_3_rpg/service/firebase_auth_service.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class RegisterPage extends StatefulWidget {
  const RegisterPage({super.key});

  @override
  State<RegisterPage> createState() => _RegisterPageState();
}

class _RegisterPageState extends State<RegisterPage> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final _confirmPasswordController = TextEditingController();
  final _authService = FirebaseAuthService();
  final TextStyle _titleStyle = GoogleFonts.cinzel();
  final TextStyle _fontStyle = GoogleFonts.roboto();

  void showWaiting() {
    showDialog(
      context: context,
      builder: (context) {
        return Center(child: CircularProgressIndicator(color: Colors.brown[800]));
      },
    );
  }

  void showAlert(String title, String msg) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          backgroundColor: const Color(0xFFEFEBE9),
          title: Text(
            title,
            style: _titleStyle.copyWith(fontWeight: FontWeight.bold, color: Colors.brown[900]),
          ),
          content: Text(msg, style: _fontStyle.copyWith(color: Colors.brown[800])),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: Text(
                'OK',
                style: _fontStyle.copyWith(color: Colors.brown[900], fontWeight: FontWeight.bold),
              ),
            ),
          ],
        );
      },
    );
  }

  String? validatePassword(String password) {
    if (password.length < 6) {
      return 'The password must contain at least six characters.';
    }
    if (!password.contains(RegExp(r'[A-Z]'))) {
      return 'The password must contain at least one uppercase letter.';
    }
    if (!password.contains(RegExp(r'[0-9]'))) {
      return 'The password must contain at least one number.';
    }
    if (!password.contains(RegExp(r'[!@#\$&*~^%().,?"{}:|<>]'))) {
      return 'The password must contain at least one special character (@, #, &).';
    }

    return null;
  }

  void registerUser() async {
    if (_emailController.text.isEmpty ||
        _passwordController.text.isEmpty ||
        _confirmPasswordController.text.isEmpty) {
      showAlert('Alert', 'Please make sure to fill in all fields.');
      return;
    }
    if (_passwordController.text != _confirmPasswordController.text) {
      showAlert('Alert', 'Passwords do not match.');
      return;
    }
    String? passwordError = validatePassword(_passwordController.text);
    if (passwordError != null) {
      showAlert('Weak Password', passwordError);
      return;
    }

    showWaiting();
    try {
      await _authService.signUp(_emailController.text, _passwordController.text);
      await _authService.sendEmailVerification();

      if (!mounted) return;
      Navigator.pop(context);

      await showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            backgroundColor: const Color(0xFFEFEBE9),
            title: Text(
              'Almost There!',
              style: _titleStyle.copyWith(fontWeight: FontWeight.bold, color: Colors.brown[900]),
            ),
            content: Text(
              'We have sent a verification link to your email. Please check your inbox and spam folder.',
              style: _fontStyle.copyWith(color: Colors.brown[800]),
            ),
            actions: [
              TextButton(
                onPressed: () => Navigator.pop(context),
                child: Text(
                  'OK',
                  style: _fontStyle.copyWith(color: Colors.brown[900], fontWeight: FontWeight.bold),
                ),
              ),
            ],
          );
        },
      );

      if (!mounted) return;
      Navigator.pop(context);
    } on FirebaseAuthException catch (e) {
      if (!mounted) return;
      Navigator.pop(context);

      String errorMsg = e.message ?? 'An unknown error occurred.';

      if (e.code == 'email-already-in-use') {
        errorMsg = 'This email is already linked to another account.';
      } else if (e.code == 'invalid-email') {
        errorMsg = 'Please provide a valid email address (example@email.com).';
      }

      showAlert('Error', errorMsg);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF5E6CB),
      appBar: AppBar(
        backgroundColor: Colors.transparent,
        elevation: 0,
        leading: IconButton(
          icon: Icon(Icons.arrow_back, color: Colors.brown[900]),
          onPressed: () => Navigator.pop(context),
        ),
      ),
      body: SafeArea(
        child: SingleChildScrollView(
          child: Center(
            child: Column(
              children: <Widget>[
                const SizedBox(height: 20),
                Text(
                  'Create Account',
                  style: _titleStyle.copyWith(
                    color: Colors.brown[900],
                    fontSize: 35,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 35),
                MyTextfield(
                  controller: _emailController,
                  hintText: 'Email',
                  obscureText: false,
                  keyboardType: TextInputType.emailAddress,
                ),
                const SizedBox(height: 15),
                MyTextfield(
                  controller: _passwordController,
                  hintText: 'Password',
                  obscureText: true,
                ),
                const SizedBox(height: 15),
                MyTextfield(
                  controller: _confirmPasswordController,
                  hintText: 'Confirm Password',
                  obscureText: true,
                ),
                const SizedBox(height: 25),
                MyButton(onTap: registerUser, text: 'Sign Up'),
                const SizedBox(height: 25),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
