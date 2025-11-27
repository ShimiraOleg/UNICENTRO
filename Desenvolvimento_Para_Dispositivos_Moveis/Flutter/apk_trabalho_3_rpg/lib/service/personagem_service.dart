import 'package:cloud_firestore/cloud_firestore.dart';
import 'package:firebase_auth/firebase_auth.dart';

class PersonagemService {
  final CollectionReference personagens = FirebaseFirestore.instance.collection('personagem');
  String? get _uid => FirebaseAuth.instance.currentUser?.uid;

  Future<void> create({
    required String name,
    required String type,
    required String kindred,
    String? img,
    int level = 1,
    int str = 10,
    int dex = 10,
    int con = 10,
    int iq = 10,
    int wiz = 10,
    int cha = 10,
    int lk = 10,
    int spd = 10,
    List<String> equipment = const [],
  }) {
    if (_uid == null) throw Exception("Usuário não logado!");

    return personagens.add({
      'userId': _uid,
      'name': name,
      'type': type,
      'kindred': kindred,
      'img': img,
      'level': level,
      'equipment': equipment,
      'str': str,
      'dex': dex,
      'con': con,
      'iq': iq,
      'wiz': wiz,
      'cha': cha,
      'lk': lk,
      'spd': spd,
      'created_at': Timestamp.now(),
    });
  }

  Stream<QuerySnapshot> read() {
    if (_uid == null) return const Stream.empty();

    return personagens.where('userId', isEqualTo: _uid).snapshots();
  }

  Future<void> update(String docID, Map<String, dynamic> novosDados) {
    return personagens.doc(docID).update(novosDados);
  }

  Future<void> delete(String docID) {
    return personagens.doc(docID).delete();
  }
}
