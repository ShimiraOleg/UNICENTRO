import 'dart:io';
import 'package:apk_trabalho_2_rpg/components/my_button.dart';
import 'package:apk_trabalho_2_rpg/database/helper/sheet_helper.dart';
import 'package:apk_trabalho_2_rpg/database/model/sheet_model.dart';
import 'package:apk_trabalho_2_rpg/view/character_sheet_page.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

enum OrderOptions { orderAZ, orderZA, orderLevel }

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final SheetHelper helper = SheetHelper();
  final TextEditingController _searchController = TextEditingController();
  List<Character> _allCharacters = [];
  List<Character> _filteredCharacters = [];
  final TextStyle _titleStyle = GoogleFonts.cinzel();
  final TextStyle _fontStyle = GoogleFonts.roboto();

  @override
  void initState() {
    super.initState();
    _loadCharacters();
  }

  void _loadCharacters() {
    helper.getAllCharacters().then((list) {
      setState(() {
        _allCharacters = list;
        _filteredCharacters = _searchController.text.isNotEmpty
            ? _filterList(_searchController.text)
            : list;
      });
    });
  }

  List<Character> _filterList(String query) {
    final queryLower = query.toLowerCase();

    return _allCharacters.where((char) {
      final nameLower = char.name.toLowerCase();
      bool startsFull = nameLower.startsWith(queryLower);
      bool startsPart = nameLower.split(' ').any((part) => part.startsWith(queryLower));
      return startsFull || startsPart;
    }).toList();
  }

  void _filterCharacters(String query) {
    setState(() {
      _filteredCharacters = query.isEmpty ? _allCharacters : _filterList(query);
    });
  }

  void _orderList(OrderOptions result) {
    setState(() {
      switch (result) {
        case OrderOptions.orderAZ:
          _filteredCharacters.sort((a, b) => a.name.toLowerCase().compareTo(b.name.toLowerCase()));
          break;
        case OrderOptions.orderZA:
          _filteredCharacters.sort((a, b) => b.name.toLowerCase().compareTo(a.name.toLowerCase()));
          break;
        case OrderOptions.orderLevel:
          _filteredCharacters.sort((a, b) => b.level.compareTo(a.level));
          break;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return Theme(
      data: Theme.of(
        context,
      ).copyWith(textTheme: GoogleFonts.cinzelTextTheme(Theme.of(context).textTheme)),
      child: Scaffold(
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
          ],
        ),
        backgroundColor: const Color(0xFFF5E6CB),
        body: Column(
          children: [
            Padding(
              padding: const EdgeInsets.fromLTRB(10, 15, 10, 10),
              child: TextField(
                controller: _searchController,
                onChanged: _filterCharacters,
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
                            _filterCharacters("");
                          },
                        )
                      : null,
                ),
              ),
            ),
            Expanded(
              child: _filteredCharacters.isEmpty
                  ? Center(
                      child: Text(
                        "No Character Found...",
                        style: _fontStyle.copyWith(fontSize: 18, color: Colors.brown),
                      ),
                    )
                  : ListView.builder(
                      padding: const EdgeInsets.symmetric(horizontal: 10.0),
                      itemCount: _filteredCharacters.length,
                      itemBuilder: (context, index) =>
                          _characterCard(context, _filteredCharacters[index]),
                    ),
            ),
            Padding(
              padding: const EdgeInsets.all(20.0),
              child: MyButton(text: "CREATE NEW CHARACTER", onTap: () => _showCharacterPage()),
            ),
          ],
        ),
      ),
    );
  }

  Widget _characterCard(BuildContext context, Character character) {
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
                  image: DecorationImage(
                    image: character.img != null && character.img!.isNotEmpty
                        ? FileImage(File(character.img!)) as ImageProvider
                        : const AssetImage("assets/imgs/profile_placeholder.jpg"),
                    fit: BoxFit.cover,
                  ),
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

  void _showCharacterPage({Character? character}) async {
    final recCharacter = await Navigator.push(
      context,
      MaterialPageRoute(builder: (context) => CharacterSheetPage(character: character)),
    );
    if (recCharacter != null) _loadCharacters();
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
              onPressed: () {
                if (character.id != null) {
                  helper.deleteCharacter(character.id!);
                  setState(() {
                    _allCharacters.removeWhere((element) => element.id == character.id);
                    _filterCharacters(_searchController.text);
                  });
                }
                Navigator.of(context).pop();
              },
            ),
          ],
        );
      },
    );
  }
}
