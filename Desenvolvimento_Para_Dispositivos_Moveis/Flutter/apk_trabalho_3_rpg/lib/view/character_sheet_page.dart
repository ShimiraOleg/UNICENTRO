import 'dart:io';
import 'package:apk_trabalho_3_rpg/components/my_button.dart';
import 'package:apk_trabalho_3_rpg/models/character_model.dart';
import 'package:apk_trabalho_3_rpg/service/personagem_service.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:image_picker/image_picker.dart';
import 'package:google_fonts/google_fonts.dart';

class CharacterSheetPage extends StatefulWidget {
  final Character? character;
  final bool isReadOnly;
  const CharacterSheetPage({super.key, this.character, this.isReadOnly = false});

  @override
  State<CharacterSheetPage> createState() => _CharacterSheetPageState();
}

class _CharacterSheetPageState extends State<CharacterSheetPage> {
  final _service = PersonagemService();
  Character? _editedCharacter;
  bool _userEdited = false;
  final ImagePicker _picker = ImagePicker();
  final _nameController = TextEditingController();
  final _levelController = TextEditingController();
  final _equipController = TextEditingController();
  final _strController = TextEditingController();
  final _conController = TextEditingController();
  final _dexController = TextEditingController();
  final _spdController = TextEditingController();
  final _lkController = TextEditingController();
  final _iqController = TextEditingController();
  final _wizController = TextEditingController();
  final _chaController = TextEditingController();
  final TextStyle _fontStyle = GoogleFonts.roboto(color: Colors.brown[900]);
  final List<String> _kindredList = ['-', 'Dwarf', 'Elf', 'Fairy', 'Hobb', 'Human', 'Leprechaun'];
  final List<String> _typeList = ['-', 'Warrior', 'Rogue', 'Wizard', 'Specialist'];
  String? _selectedKindred;
  String? _selectedType;
  final numberInputFormatter = FilteringTextInputFormatter.allow(RegExp(r'[0-9]'));

  @override
  void initState() {
    super.initState();

    if (widget.character == null) {
      _editedCharacter = Character(
        userId: "",
        name: "",
        kindred: "-",
        type: "-",
        level: 1,
        str: 10,
        con: 10,
        dex: 10,
        spd: 10,
        lk: 10,
        iq: 10,
        wiz: 10,
        cha: 10,
        equipment: [],
        img: null,
      );

      _selectedKindred = "-";
      _selectedType = "-";
      _levelController.text = "1";
      _setStatsControllers(10);
    } else {
      _editedCharacter = widget.character;
      _nameController.text = _editedCharacter!.name;
      _selectedKindred = _kindredList.contains(_editedCharacter!.kindred)
          ? _editedCharacter!.kindred
          : "-";
      _selectedType = _typeList.contains(_editedCharacter!.type) ? _editedCharacter!.type : "-";
      _levelController.text = _editedCharacter!.level.toString();
      _strController.text = _editedCharacter!.str.toString();
      _conController.text = _editedCharacter!.con.toString();
      _dexController.text = _editedCharacter!.dex.toString();
      _spdController.text = _editedCharacter!.spd.toString();
      _lkController.text = _editedCharacter!.lk.toString();
      _iqController.text = _editedCharacter!.iq.toString();
      _wizController.text = _editedCharacter!.wiz.toString();
      _chaController.text = _editedCharacter!.cha.toString();
      _equipController.text = _editedCharacter!.equipment.join('\n');
    }
  }

  void _setStatsControllers(int value) {
    String v = value.toString();
    _strController.text = v;
    _conController.text = v;
    _dexController.text = v;
    _spdController.text = v;
    _lkController.text = v;
    _iqController.text = v;
    _wizController.text = v;
    _chaController.text = v;
  }

  void showAlert(String msg) {
    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: const Text("Alert"),
          content: Text(msg, style: _fontStyle),
          actions: [TextButton(onPressed: () => Navigator.pop(context), child: const Text('OK'))],
        );
      },
    );
  }

  ImageProvider _getImageProvider() {
    if (_editedCharacter?.img != null && _editedCharacter!.img!.isNotEmpty) {
      if (_editedCharacter!.img!.startsWith('http')) {
        return NetworkImage(_editedCharacter!.img!);
      }
      return FileImage(File(_editedCharacter!.img!));
    }
    return const AssetImage("assets/imgs/profile_placeholder.jpg");
  }

  @override
  Widget build(BuildContext context) {
    return PopScope(
      canPop: widget.isReadOnly,
      onPopInvokedWithResult: (bool didPop, dynamic result) async {
        if (didPop) return;

        final bool shouldPop = await _requestPop();
        if (shouldPop && context.mounted) {
          Navigator.of(context).pop();
        }
      },
      child: GestureDetector(
        onTap: () {
          FocusScope.of(context).unfocus();
        },
        child: Scaffold(
          backgroundColor: const Color(0xFFF5E6CB),
          appBar: AppBar(
            backgroundColor: Colors.brown[800],
            title: Text(
              widget.isReadOnly
                  ? "View Character Sheet"
                  : (_editedCharacter?.id != null ? "Edit Character" : "New Character"),
              style: GoogleFonts.cinzel(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            centerTitle: true,
            foregroundColor: Colors.white,
          ),
          body: SingleChildScrollView(
            padding: const EdgeInsets.all(10.0),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: <Widget>[
                GestureDetector(
                  onTap: widget.isReadOnly ? null : _selectImage,
                  child: Center(
                    child: Container(
                      width: 140.0,
                      height: 140.0,
                      decoration: BoxDecoration(
                        shape: BoxShape.circle,
                        border: Border.all(color: Colors.brown, width: 4),
                        image: DecorationImage(image: _getImageProvider(), fit: BoxFit.cover),
                      ),
                      child: !widget.isReadOnly
                          ? const Icon(Icons.add_a_photo, size: 50, color: Colors.brown)
                          : null,
                    ),
                  ),
                ),
                const SizedBox(height: 20),
                Container(
                  decoration: BoxDecoration(
                    border: Border.all(color: Colors.brown[800]!, width: 2),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  padding: const EdgeInsets.all(16),
                  child: Column(
                    children: [
                      Text(
                        "Tunnels & Trolls Character Sheet",
                        style: GoogleFonts.cinzel(fontSize: 18, fontWeight: FontWeight.bold),
                      ),
                      const SizedBox(height: 15),

                      Row(
                        children: [
                          Expanded(flex: 3, child: _buildTextField(_nameController, "Name")),
                          const SizedBox(width: 10),
                          Expanded(
                            flex: 1,
                            child: _buildTextField(_levelController, "Level", isNumber: true),
                          ),
                        ],
                      ),
                      const SizedBox(height: 10),
                      Row(
                        children: [
                          Expanded(
                            child: _buildDropdown("Kindred", _kindredList, _selectedKindred, (val) {
                              setState(() {
                                _selectedKindred = val;
                                _userEdited = true;
                              });
                            }),
                          ),
                          const SizedBox(width: 10),
                          Expanded(
                            child: _buildDropdown("Type", _typeList, _selectedType, (val) {
                              setState(() {
                                _selectedType = val;
                                _userEdited = true;
                              });
                            }),
                          ),
                        ],
                      ),
                      const SizedBox(height: 20),
                      const Divider(color: Colors.brown),
                      Text(
                        "ATTRIBUTES",
                        style: GoogleFonts.cinzel(fontSize: 18, fontWeight: FontWeight.bold),
                      ),
                      const SizedBox(height: 10),
                      GridView.count(
                        crossAxisCount: 4,
                        crossAxisSpacing: 10,
                        mainAxisSpacing: 10,
                        shrinkWrap: true,
                        physics: const NeverScrollableScrollPhysics(),
                        childAspectRatio: 0.9,
                        children: [
                          _buildStatBox("STR", _strController),
                          _buildStatBox("CON", _conController),
                          _buildStatBox("DEX", _dexController),
                          _buildStatBox("SPD", _spdController),
                          _buildStatBox("LK", _lkController),
                          _buildStatBox("IQ", _iqController),
                          _buildStatBox("WIZ", _wizController),
                          _buildStatBox("CHA", _chaController),
                        ],
                      ),
                      const Divider(color: Colors.brown),
                      Text(
                        "EQUIPMENT",
                        style: GoogleFonts.cinzel(fontSize: 18, fontWeight: FontWeight.bold),
                      ),
                      const SizedBox(height: 5),
                      TextField(
                        controller: _equipController,
                        maxLines: 5,
                        style: _fontStyle,
                        readOnly: widget.isReadOnly,
                        onChanged: (text) => _userEdited = true,
                        decoration: InputDecoration(
                          hintText: "One item per line...",
                          border: const OutlineInputBorder(),
                          filled: true,
                          fillColor: widget.isReadOnly ? Colors.black12 : const Color(0x55FFFFFF),
                        ),
                      ),
                    ],
                  ),
                ),
                const SizedBox(height: 25),
                if (!widget.isReadOnly) MyButton(text: "SAVE CHARACTER", onTap: _saveCharacter),
                const SizedBox(height: 20),
              ],
            ),
          ),
        ),
      ),
    );
  }

  Widget _buildTextField(TextEditingController controller, String label, {bool isNumber = false}) {
    return TextField(
      controller: controller,
      style: _fontStyle,
      readOnly: widget.isReadOnly,
      keyboardType: isNumber ? TextInputType.number : TextInputType.text,
      inputFormatters: isNumber ? [numberInputFormatter] : [],
      decoration: InputDecoration(
        labelText: label,
        labelStyle: _fontStyle,
        filled: true,
        fillColor: widget.isReadOnly ? Colors.black12 : const Color(0x80FFFFFF),
        border: const OutlineInputBorder(),
      ),
      onChanged: (text) => _userEdited = true,
    );
  }

  Widget _buildDropdown(
    String label,
    List<String> items,
    String? value,
    Function(String?) onChanged,
  ) {
    return DropdownButtonFormField<String>(
      initialValue: items.contains(value) ? value : items.first,
      style: _fontStyle,
      decoration: InputDecoration(
        labelStyle: _fontStyle,
        labelText: label,
        filled: true,
        fillColor: widget.isReadOnly ? Colors.black12 : const Color(0x80FFFFFF),
        border: const OutlineInputBorder(),
      ),
      items: items.map((String item) {
        return DropdownMenuItem<String>(value: item, child: Text(item));
      }).toList(),
      onChanged: widget.isReadOnly ? null : onChanged,
    );
  }

  Widget _buildStatBox(String label, TextEditingController controller) {
    return Column(
      children: [
        Text(label, style: const TextStyle(fontWeight: FontWeight.bold)),
        SizedBox(
          width: 60,
          child: TextField(
            controller: controller,
            readOnly: widget.isReadOnly,
            textAlign: TextAlign.center,
            keyboardType: TextInputType.number,
            inputFormatters: [numberInputFormatter],
            style: _fontStyle,
            decoration: InputDecoration(
              contentPadding: const EdgeInsets.symmetric(vertical: 5),
              border: const OutlineInputBorder(),
              filled: true,
              fillColor: widget.isReadOnly ? Colors.black12 : const Color(0x80FFFFFF),
            ),
            onChanged: (text) => _userEdited = true,
          ),
        ),
      ],
    );
  }

  Future<void> _selectImage() async {
    final XFile? image = await _picker.pickImage(source: ImageSource.gallery);
    if (image != null) {
      setState(() {
        _editedCharacter?.img = image.path;
        _userEdited = true;
      });
    }
  }

  Future<bool> _requestPop() {
    if (_userEdited) {
      showDialog(
        context: context,
        builder: (context) {
          return AlertDialog(
            title: const Text("Discard changes?"),
            content: const Text("If you leave, changes will be lost"),
            actions: [
              TextButton(child: const Text("Cancel"), onPressed: () => Navigator.pop(context)),
              TextButton(
                child: const Text("Yes"),
                onPressed: () {
                  Navigator.pop(context);
                  Navigator.pop(context);
                },
              ),
            ],
          );
        },
      );
      return Future.value(false);
    } else {
      return Future.value(true);
    }
  }

  int _validateNumber(String text, String fieldName, {int min = 1, int max = 200}) {
    int? value = int.tryParse(text);
    if (value == null) {
      throw "'$fieldName' can't be empty!";
    }
    if (value < min) {
      throw "'$fieldName' can't be lower than $min!";
    }
    if (value > max) {
      throw "'$fieldName' can't be higher than $max!";
    }
    return value;
  }

  void _saveCharacter() async {
    if (_nameController.text.trim().isEmpty) {
      showAlert("Name is mandatory!");
      return;
    }
    if (_nameController.text.length > 20) {
      showAlert("Name can't be longer than 20 characters!");
      return;
    }
    if (_selectedKindred == "-" || _selectedType == "-") {
      showAlert("Please select a kindred and type!");
      return;
    }

    try {
      List<String> listEquip = [];
      if (_equipController.text.trim().isNotEmpty) {
        listEquip = _equipController.text
            .split('\n')
            .where((item) => item.trim().isNotEmpty)
            .toList();
      }
      final valLevel = _validateNumber(_levelController.text, "Level", max: 100);
      final valStr = _validateNumber(_strController.text, "STR");
      final valCon = _validateNumber(_conController.text, "CON");
      final valDex = _validateNumber(_dexController.text, "DEX");
      final valSpd = _validateNumber(_spdController.text, "SPD");
      final valLk = _validateNumber(_lkController.text, "LK");
      final valIq = _validateNumber(_iqController.text, "IQ");
      final valWiz = _validateNumber(_wizController.text, "WIZ");
      final valCha = _validateNumber(_chaController.text, "CHA");

      if (_editedCharacter!.id != null) {
        await _service.update(_editedCharacter!.id!, {
          'name': _nameController.text,
          'kindred': _selectedKindred,
          'type': _selectedType,
          'level': valLevel,
          'str': valStr,
          'con': valCon,
          'dex': valDex,
          'spd': valSpd,
          'lk': valLk,
          'iq': valIq,
          'wiz': valWiz,
          'cha': valCha,
          'equipment': listEquip,
          'img': _editedCharacter?.img,
        });
      } else {
        await _service.create(
          name: _nameController.text,
          kindred: _selectedKindred!,
          type: _selectedType!,
          level: valLevel,
          str: valStr,
          con: valCon,
          dex: valDex,
          spd: valSpd,
          lk: valLk,
          iq: valIq,
          wiz: valWiz,
          cha: valCha,
          equipment: listEquip,
          img: _editedCharacter?.img,
        );
      }

      if (mounted) {
        Navigator.pop(context);
      }
    } catch (e) {
      if (mounted) {
        showAlert("$e");
      }
    }
  }
}
