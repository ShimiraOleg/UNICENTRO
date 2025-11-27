import 'dart:io';
import 'package:apk_trabalho_3_rpg/components/my_button.dart';
import 'package:apk_trabalho_3_rpg/models/character_model.dart';
import 'package:apk_trabalho_3_rpg/service/firebase_auth_service.dart';
import 'package:apk_trabalho_3_rpg/view/character_sheet_page.dart';
import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

enum OrderOptions { orderAZ, orderZA, orderLevel }

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final _firestore = FirebaseFirestore.instance;
  final User? _currentUser = FirebaseAuth.instance.currentUser;
  final _searchController = TextEditingController();
  final _authService = FirebaseAuthService();
  OrderOptions _currentOrder = OrderOptions.orderAZ;
  final TextStyle _titleStyle = GoogleFonts.cinzel();
  final TextStyle _fontStyle = GoogleFonts.roboto();

  void _showLogoutConfirmation(BuildContext context) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          backgroundColor: const Color(0xFFEFEBE9),
          title: Text("Logout", style: _fontStyle.copyWith(fontWeight: FontWeight.bold)),
          content: Text("Do you really wish to logout?", style: _fontStyle),
          actions: <Widget>[
            TextButton(
              child: Text("Cancel", style: _fontStyle.copyWith(color: Colors.black)),
              onPressed: () => Navigator.of(context).pop(),
            ),
            TextButton(
              child: Text("Yes, Logout", style: _fontStyle.copyWith(color: Colors.red)),
              onPressed: () async {
                Navigator.of(context).pop();
                await _authService.signOut();
              },
            ),
          ],
        );
      },
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(
          "Characters",
          style: _titleStyle.copyWith(fontSize: 24, fontWeight: FontWeight.bold),
        ),
        backgroundColor: Colors.brown[800],
        foregroundColor: Colors.white,
        centerTitle: true,
        actions: <Widget>[
          PopupMenuButton<OrderOptions>(
            icon: const Icon(Icons.sort),
            color: const Color(0xFFEFEBE9),
            itemBuilder: (context) => [
              const PopupMenuItem(value: OrderOptions.orderAZ, child: Text("A-Z")),
              const PopupMenuItem(value: OrderOptions.orderZA, child: Text("Z-A")),
              const PopupMenuItem(value: OrderOptions.orderLevel, child: Text("Level")),
            ],
            onSelected: _orderList,
          ),
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () => _showLogoutConfirmation(context),
            tooltip: "Logout",
          ),
        ],
      ),
      backgroundColor: const Color(0xFFF5E6CB),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.fromLTRB(10, 15, 10, 10),
            child: TextField(
              controller: _searchController,
              onChanged: (text) {
                setState(() {});
              },
              style: TextStyle(color: Colors.brown[900]),
              decoration: InputDecoration(
                labelText: "Search characters",
                labelStyle: TextStyle(color: Colors.brown[800]),
                hintText: "Character Name...",
                fillColor: const Color(0xFFEFEBE9),
                filled: true,
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(8.0),
                  borderSide: BorderSide(color: Colors.brown[800]!),
                ),
                enabledBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(8.0),
                  borderSide: BorderSide(color: Colors.brown[300]!),
                ),
                focusedBorder: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(8.0),
                  borderSide: BorderSide(color: Colors.brown[800]!, width: 2),
                ),
                prefixIcon: Icon(Icons.search, color: Colors.brown[800]),
                suffixIcon: _searchController.text.isNotEmpty
                    ? IconButton(
                        icon: Icon(Icons.clear, color: Colors.brown[600]),
                        onPressed: () {
                          _searchController.clear();
                          setState(() {});
                        },
                      )
                    : null,
              ),
            ),
          ),

          Expanded(
            child: StreamBuilder<QuerySnapshot>(
              stream: _firestore
                  .collection('personagem')
                  .where('userId', isEqualTo: _currentUser?.uid)
                  .snapshots(),
              builder: (context, snapshot) {
                if (snapshot.connectionState == ConnectionState.waiting) {
                  return const Center(child: CircularProgressIndicator(color: Colors.brown));
                }
                List<Character> listaPersonagens = [];
                try {
                  listaPersonagens = snapshot.data!.docs.map((doc) {
                    Map<String, dynamic> data = doc.data() as Map<String, dynamic>;
                    return Character.fromMap(data, doc.id);
                  }).toList();
                } catch (e) {
                  return Center(child: Text("$e"));
                }
                if (_searchController.text.isNotEmpty) {
                  final queryLower = _searchController.text.toLowerCase();
                  listaPersonagens = listaPersonagens.where((char) {
                    final nameLower = char.name.toLowerCase();
                    bool startsFull = nameLower.startsWith(queryLower);
                    bool startsPart = nameLower
                        .split(' ')
                        .any((part) => part.startsWith(queryLower));
                    return startsFull || startsPart;
                  }).toList();
                }
                switch (_currentOrder) {
                  case OrderOptions.orderAZ:
                    listaPersonagens.sort(
                      (a, b) => a.name.toLowerCase().compareTo(b.name.toLowerCase()),
                    );
                    break;
                  case OrderOptions.orderZA:
                    listaPersonagens.sort(
                      (a, b) => b.name.toLowerCase().compareTo(a.name.toLowerCase()),
                    );
                    break;
                  case OrderOptions.orderLevel:
                    listaPersonagens.sort((a, b) => b.level.compareTo(a.level));
                    break;
                }
                if (listaPersonagens.isEmpty) {
                  return Center(
                    child: Text(
                      "No characters found...",
                      style: _fontStyle.copyWith(fontSize: 18, color: Colors.brown),
                    ),
                  );
                }

                return ListView.builder(
                  padding: const EdgeInsets.symmetric(horizontal: 10.0),
                  itemCount: listaPersonagens.length,
                  itemBuilder: (context, index) => _characterCard(context, listaPersonagens[index]),
                );
              },
            ),
          ),

          Padding(
            padding: const EdgeInsets.all(20.0),
            child: MyButton(text: "CREATE NEW CHARACTER", onTap: () => _showCharacterPage()),
          ),
        ],
      ),
    );
  }

  void _orderList(OrderOptions result) {
    setState(() {
      _currentOrder = result;
    });
  }

  Widget _characterCard(BuildContext context, Character character) {
    ImageProvider imgProvider;
    if (character.img != null && character.img!.isNotEmpty) {
      if (character.img!.startsWith('http')) {
        imgProvider = NetworkImage(character.img!);
      } else {
        imgProvider = FileImage(File(character.img!));
      }
    } else {
      imgProvider = const AssetImage("assets/imgs/profile_placeholder.jpg");
    }

    return GestureDetector(
      onTap: () {
        Navigator.push(
          context,
          MaterialPageRoute(
            builder: (context) => CharacterSheetPage(character: character, isReadOnly: true),
          ),
        );
      },
      child: Card(
        color: const Color(0xFFEFEBE9),
        elevation: 4,
        margin: const EdgeInsets.symmetric(vertical: 6.0),
        child: Padding(
          padding: const EdgeInsets.all(8.0),
          child: Row(
            children: <Widget>[
              Container(
                width: 70.0,
                height: 70.0,
                decoration: BoxDecoration(
                  shape: BoxShape.rectangle,
                  borderRadius: BorderRadius.circular(8),
                  border: Border.all(color: Colors.brown, width: 2),
                  image: DecorationImage(image: imgProvider, fit: BoxFit.cover),
                ),
              ),
              const SizedBox(width: 15),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: <Widget>[
                    Text(
                      character.name,
                      style: _fontStyle.copyWith(
                        fontSize: 20.0,
                        fontWeight: FontWeight.bold,
                        color: Colors.brown[900],
                      ),
                    ),
                    const SizedBox(height: 4),
                    Text(
                      "Level ${character.level} | ${character.kindred}",
                      style: _fontStyle.copyWith(
                        fontSize: 14.0,
                        fontWeight: FontWeight.w600,
                        color: Colors.brown[700],
                      ),
                    ),
                    Text(
                      character.type,
                      style: _fontStyle.copyWith(fontSize: 14.0, color: Colors.brown[600]),
                    ),
                  ],
                ),
              ),
              PopupMenuButton<String>(
                icon: Icon(Icons.more_vert, color: Colors.brown[800]),
                color: const Color(0xFFEFEBE9),
                onSelected: (String result) {
                  if (result == 'edit') {
                    _showCharacterPage(character: character);
                  } else if (result == 'delete') {
                    _showDeleteConfirmation(context, character);
                  }
                },
                itemBuilder: (BuildContext context) => <PopupMenuEntry<String>>[
                  PopupMenuItem<String>(
                    value: 'edit',
                    child: Text(
                      'Edit',
                      style: _fontStyle.copyWith(color: Colors.brown, fontWeight: FontWeight.bold),
                    ),
                  ),
                  PopupMenuItem<String>(
                    value: 'delete',
                    child: Text('Delete', style: _fontStyle.copyWith(color: Colors.red)),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }

  void _showCharacterPage({Character? character}) {
    Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => CharacterSheetPage(character: character)),
    );
  }

  void _showDeleteConfirmation(BuildContext context, Character character) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          backgroundColor: const Color(0xFFEFEBE9),
          title: Text("Delete Character", style: _fontStyle.copyWith(fontWeight: FontWeight.bold)),
          content: Text("Do you really wish to delete ${character.name}?", style: _fontStyle),
          actions: <Widget>[
            TextButton(
              child: Text("Cancel", style: _fontStyle.copyWith(color: Colors.black)),
              onPressed: () => Navigator.of(context).pop(),
            ),
            TextButton(
              child: Text("Yes, Delete", style: _fontStyle.copyWith(color: Colors.red)),
              onPressed: () async {
                if (character.id == null || character.id!.isEmpty) {
                  return;
                }

                try {
                  await _firestore.collection('personagem').doc(character.id).delete();

                  if (context.mounted) {
                    Navigator.of(context).pop();
                  }
                } catch (e) {
                  if (context.mounted) {
                    Navigator.of(context).pop();
                    ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text("$e")));
                  }
                }
              },
            ),
          ],
        );
      },
    );
  }
}
