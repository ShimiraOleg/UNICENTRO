import 'package:apk_trabalho_3_rpg/firebase_options.dart';
import 'package:apk_trabalho_3_rpg/view/auth_page.dart';
import 'package:firebase_core/firebase_core.dart';
import 'package:flutter/material.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Firebase.initializeApp(options: DefaultFirebaseOptions.currentPlatform);
  runApp(MaterialApp(home: AuthPage(), debugShowCheckedModeBanner: false));
}
