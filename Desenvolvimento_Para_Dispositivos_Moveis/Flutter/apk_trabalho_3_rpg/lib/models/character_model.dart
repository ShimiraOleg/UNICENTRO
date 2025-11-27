class Character {
  String? id;
  String userId;
  String name;
  String type;
  String kindred;
  int level;
  String? img;
  int str;
  int dex;
  int con;
  int iq;
  int wiz;
  int cha;
  int lk;
  int spd;
  List<String> equipment;

  Character({
    this.id,
    required this.userId,
    required this.name,
    required this.type,
    required this.kindred,
    required this.level,
    this.img,
    this.str = 10,
    this.dex = 10,
    this.con = 10,
    this.iq = 10,
    this.wiz = 10,
    this.cha = 10,
    this.lk = 10,
    this.spd = 10,
    this.equipment = const [],
  });

  factory Character.fromMap(Map<String, dynamic> map, String docId) {
    return Character(
      id: docId,
      userId: map['userId'] ?? '',
      name: map['name'] ?? 'Sem Nome',
      type: map['type'] ?? '',
      kindred: map['kindred'] ?? '',
      level: map['level'] is int ? map['level'] : int.tryParse(map['level'].toString()) ?? 1,
      img: map['img'],
      str: map['str'] ?? 10,
      dex: map['dex'] ?? 10,
      con: map['con'] ?? 10,
      iq: map['iq'] ?? 10,
      wiz: map['wiz'] ?? 10,
      cha: map['cha'] ?? 10,
      lk: map['lk'] ?? 10,
      spd: map['spd'] ?? 10,
      equipment: List<String>.from(map['equipment'] ?? []),
    );
  }

  Map<String, dynamic> toMap() {
    return {
      'userId': userId,
      'name': name,
      'type': type,
      'kindred': kindred,
      'level': level,
      'img': img,
      'str': str,
      'dex': dex,
      'con': con,
      'iq': iq,
      'wiz': wiz,
      'cha': cha,
      'lk': lk,
      'spd': spd,
      'equipment': equipment,
    };
  }
}
