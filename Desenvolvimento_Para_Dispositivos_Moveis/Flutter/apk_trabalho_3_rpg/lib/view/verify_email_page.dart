import 'dart:async';
import 'package:apk_trabalho_3_rpg/components/my_button.dart';
import 'package:apk_trabalho_3_rpg/service/firebase_auth_service.dart';
import 'package:apk_trabalho_3_rpg/view/home_page.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

class VerifyEmailPage extends StatefulWidget {
  const VerifyEmailPage({super.key});

  @override
  State<VerifyEmailPage> createState() => _VerifyEmailPageState();
}

class _VerifyEmailPageState extends State<VerifyEmailPage> {
  bool isEmailVerified = false;
  Timer? timer;
  final _authService = FirebaseAuthService();
  final TextStyle _titleStyle = GoogleFonts.cinzel();
  final TextStyle _fontStyle = GoogleFonts.roboto();

  @override
  void initState() {
    super.initState();
    isEmailVerified = _authService.isEmailVerified;

    if (!isEmailVerified) {
      timer = Timer.periodic(const Duration(seconds: 3), (_) => checkEmailVerified());
    }
  }

  @override
  void dispose() {
    timer?.cancel();
    super.dispose();
  }

  Future checkEmailVerified() async {
    await _authService.reloadUser();
    setState(() {
      isEmailVerified = _authService.isEmailVerified;
    });

    if (isEmailVerified) {
      timer?.cancel();
    }
  }

  Future sendVerificationEmail() async {
    try {
      await _authService.sendEmailVerification();
      if (!mounted) return;

      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
            'Verification email resent!',
            style: _fontStyle.copyWith(color: Colors.white),
          ),
          backgroundColor: Colors.brown[800],
        ),
      );
    } catch (e) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(
          content: Text(
            'Error sending email: ${e.toString()}',
            style: _fontStyle.copyWith(color: Colors.white),
          ),
          backgroundColor: Colors.red[800],
        ),
      );
    }
  }

  @override
  Widget build(BuildContext context) {
    if (isEmailVerified) {
      return const HomePage();
    }
    return Scaffold(
      backgroundColor: const Color(0xFFF5E6CB),
      body: SafeArea(
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 25.0),
          child: Center(
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(Icons.mark_email_unread_outlined, size: 100, color: Colors.brown[800]),
                const SizedBox(height: 25),
                Text(
                  'Verify your email',
                  style: _titleStyle.copyWith(
                    color: Colors.brown[900],
                    fontSize: 30,
                    fontWeight: FontWeight.bold,
                  ),
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: 15),
                Text(
                  'We have sent a verification link to:',
                  style: _fontStyle.copyWith(fontSize: 16, color: Colors.brown[700]),
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: 5),
                Text(
                  FirebaseAuth.instance.currentUser!.email ?? '',
                  style: _fontStyle.copyWith(
                    fontSize: 18,
                    fontWeight: FontWeight.bold,
                    color: Colors.brown[900],
                  ),
                  textAlign: TextAlign.center,
                ),
                const SizedBox(height: 30),
                MyButton(onTap: sendVerificationEmail, text: 'Resend Email'),
                const SizedBox(height: 15),
                GestureDetector(
                  onTap: () => FirebaseAuth.instance.signOut(),
                  child: Text(
                    'Cancel',
                    style: _fontStyle.copyWith(
                      color: Colors.brown[900],
                      fontWeight: FontWeight.bold,
                      decoration: TextDecoration.underline,
                      decorationColor: Colors.brown[900],
                    ),
                  ),
                ),
              ],
            ),
          ),
        ),
      ),
    );
  }
}
