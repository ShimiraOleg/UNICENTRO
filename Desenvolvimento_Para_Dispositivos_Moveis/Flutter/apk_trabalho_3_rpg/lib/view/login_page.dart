import 'package:apk_trabalho_3_rpg/components/my_button.dart';
import 'package:apk_trabalho_3_rpg/components/my_textfield.dart';
import 'package:apk_trabalho_3_rpg/service/firebase_auth_service.dart';
import 'package:apk_trabalho_3_rpg/view/register_page.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});
  @override
  State<LoginPage> createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final _authService = FirebaseAuthService();
  final TextStyle _titleStyle = GoogleFonts.cinzel();
  final TextStyle _fontStyle = GoogleFonts.roboto();

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

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: const Color(0xFFF5E6CB),
      body: SafeArea(
        child: SingleChildScrollView(
          child: Center(
            child: Column(
              children: <Widget>[
                const SizedBox(height: 50),
                Image.asset('assets/imgs/logo.png', width: 100, height: 100, fit: BoxFit.contain),
                const SizedBox(height: 25),
                Text(
                  'Tunnels & Trolls',
                  style: _titleStyle.copyWith(
                    color: Colors.brown[900],
                    fontSize: 42,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                Text(
                  'Welcome',
                  style: _titleStyle.copyWith(
                    color: Colors.brown[800],
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                  ),
                ),
                const SizedBox(height: 25),
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
                Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 25),
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: <Widget>[
                      GestureDetector(
                        onTap: passwordReset,
                        child: Text(
                          'Forgot your password?',
                          style: _fontStyle.copyWith(
                            color: Colors.brown[900],
                            decoration: TextDecoration.underline,
                            decorationColor: Colors.brown[900],
                            fontWeight: FontWeight.bold,
                            fontSize: 16,
                          ),
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 15),
                MyButton(onTap: signUserIn, text: 'Log In'),
                const SizedBox(height: 25),
                Row(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: <Widget>[
                    Text(
                      "Don't have an account?",
                      style: _fontStyle.copyWith(color: Colors.brown[800], fontSize: 16),
                    ),
                    const SizedBox(width: 4),
                    GestureDetector(
                      onTap: () {
                        Navigator.push(
                          context,
                          MaterialPageRoute(builder: (context) => const RegisterPage()),
                        );
                      },
                      child: Text(
                        'Sign Up',
                        style: _fontStyle.copyWith(
                          color: Colors.brown[900],
                          fontWeight: FontWeight.bold,
                          decoration: TextDecoration.underline,
                          decorationColor: Colors.brown[900],
                          fontSize: 17,
                        ),
                      ),
                    ),
                  ],
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }

  String handlePasswordResetError(FirebaseAuthException e) {
    switch (e.code) {
      case 'invalid-email':
        return 'The email address is invalid.';
      default:
        return 'An error has occurred. Please verify if the typed email is correct.';
    }
  }

  void passwordReset() {
    final resetEmailController = TextEditingController();
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          backgroundColor: const Color(0xFFEFEBE9),
          title: Text(
            'Reset your password',
            style: _titleStyle.copyWith(fontWeight: FontWeight.bold, color: Colors.brown[900]),
          ),
          content: Column(
            mainAxisSize: MainAxisSize.min,
            children: [
              Text(
                'Type here your email to receive the password reset link.',
                style: _fontStyle.copyWith(color: Colors.brown[800]),
              ),
              const SizedBox(height: 10),
              MyTextfield(
                controller: resetEmailController,
                hintText: "example@email.com",
                obscureText: false,
                keyboardType: TextInputType.emailAddress,
              ),
            ],
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: Text('Cancel', style: _fontStyle.copyWith(color: Colors.brown[700])),
            ),
            TextButton(
              onPressed: () async {
                if (resetEmailController.text.isEmpty) {
                  return;
                }
                try {
                  await _authService.sendPasswordResetEmail(resetEmailController.text.trim());
                  if (!mounted) return;
                  Navigator.pop(context);
                  showDialog(
                    context: context,
                    builder: (context) => AlertDialog(
                      backgroundColor: const Color(0xFFEFEBE9),
                      title: Text(
                        'Email sent!',
                        style: _titleStyle.copyWith(fontWeight: FontWeight.bold),
                      ),
                      content: Text(
                        'Please check your inbox and spam folder, then follow the steps in the email to reset your password.',
                        style: _fontStyle,
                      ),
                      actions: [
                        TextButton(
                          onPressed: () => Navigator.pop(context),
                          child: Text('OK', style: _fontStyle.copyWith(color: Colors.brown[900])),
                        ),
                      ],
                    ),
                  );
                } on FirebaseAuthException catch (e) {
                  if (!mounted) return;
                  Navigator.pop(context);
                  showAlert('Alert', handlePasswordResetError(e));
                }
              },
              child: Text(
                'Send email',
                style: _fontStyle.copyWith(color: Colors.brown[900], fontWeight: FontWeight.bold),
              ),
            ),
          ],
        );
      },
    );
  }

  void signUserIn() async {
    if (_emailController.text.isEmpty || _passwordController.text.isEmpty) {
      showAlert('Alert', 'Please make sure to fill all fields');
      return;
    }

    showDialog(
      context: context,
      builder: (context) {
        return Center(child: CircularProgressIndicator(color: Colors.brown[800]));
      },
    );

    try {
      await _authService.signIn(_emailController.text, _passwordController.text);
      if (!mounted) return;
      Navigator.pop(context);
    } on FirebaseAuthException {
      if (!mounted) return;
      Navigator.pop(context);
      String errorMsg = 'Incorrect user or password!';
      showAlert('Alert', errorMsg);
    }
  }
}
