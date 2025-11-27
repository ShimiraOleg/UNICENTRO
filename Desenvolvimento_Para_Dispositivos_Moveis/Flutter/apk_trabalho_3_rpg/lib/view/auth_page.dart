import 'package:apk_trabalho_3_rpg/service/firebase_auth_service.dart';
import 'package:apk_trabalho_3_rpg/view/home_page.dart';
import 'package:apk_trabalho_3_rpg/view/login_page.dart';
import 'package:apk_trabalho_3_rpg/view/verify_email_page.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';

class AuthPage extends StatelessWidget {
  AuthPage({super.key});
  final _authService = FirebaseAuthService();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: StreamBuilder<User?>(
        stream: _authService.authStateChanges,
        builder: (context, snapshot) {
          if (snapshot.hasData) {
            final user = snapshot.data!;
            if (user.emailVerified) {
              return HomePage();
            } else {
              return const VerifyEmailPage();
            }
          } else {
            return const LoginPage();
          }
        },
      ),
    );
  }
}
