import 'dart:convert';

String idColumn = "idColumn";
String nameColumn = "nameColumn";
String imgColumn = "imgColumn";
String kindredColumn = "kindredColumn";
String typeColumn = "typeColumn";
String levelColumn = "levelColumn";
String strColumn = "strColumn";
String conColumn = "conColumn";
String dexColumn = "dexColumn";
String spdColumn = "spdColumn";
String lkColumn = "lkColumn";
String iqColumn = "iqColumn";
String wizColumn = "wizColumn";
String chaColumn = "chaColumn";
String equipColumn = "equipColumn";

class Character {
  Character({
    this.id,
    required this.name,
    this.img,
    required this.kindred,
    required this.type,
    required this.level,
    required this.str,
    required this.con,
    required this.dex,
    required this.spd,
    required this.lk,
    required this.iq,
    required this.wiz,
    required this.cha,
    this.equipment = const [],
  });

  int? id;
  String name;
  String? img;
  String kindred; // Selecionável
  String type; // Selecionável
  int level;
  int str;
  int con;
  int dex;
  int spd;
  int lk;
  int iq;
  int wiz;
  int cha;
  List<String> equipment;

  Character.fromMap(Map<String, dynamic> map)
    : id = map[idColumn],
      name = map[nameColumn],
      img = map[imgColumn],
      kindred = map[kindredColumn],
      type = map[typeColumn],
      level = map[levelColumn],
      str = map[strColumn],
      con = map[conColumn],
      dex = map[dexColumn],
      spd = map[spdColumn],
      lk = map[lkColumn],
      iq = map[iqColumn],
      wiz = map[wizColumn],
      cha = map[chaColumn],
      equipment = map[equipColumn] != null
          ? List<String>.from(jsonDecode(map[equipColumn]) ?? [])
          : [];

  Map<String, dynamic> toMap() {
    Map<String, dynamic> map = {
      nameColumn: name,
      imgColumn: img,
      kindredColumn: kindred,
      typeColumn: type,
      levelColumn: level,
      strColumn: str,
      conColumn: con,
      dexColumn: dex,
      spdColumn: spd,
      lkColumn: lk,
      iqColumn: iq,
      wizColumn: wiz,
      chaColumn: cha,
      equipColumn: jsonEncode(equipment),
    };
    if (id != null) {
      map[idColumn] = id;
    }
    return map;
  }

  @override
  String toString() {
    return "Character(id: $id, name: $name, kindred: $kindred, type: $type, level: $level, str: $str, con: $con, dex: $dex, spd: $spd, lk: $lk, iq: $iq, wiz: $wiz, cha: $cha, equipment: $equipment, img: $img)";
  }
}
