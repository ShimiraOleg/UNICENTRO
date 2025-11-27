import 'package:apk_trabalho_2_rpg/database/model/sheet_model.dart';
import 'package:sqflite/sqflite.dart';
import 'package:path/path.dart';

const String characterTable = "characterTable";

class SheetHelper {
  static final SheetHelper _instance = SheetHelper.internal();
  factory SheetHelper() => _instance;
  SheetHelper.internal();

  Database? _db;

  Future<Database> get db async {
    if (_db != null) {
      return _db!;
    } else {
      _db = await initDb();
      return _db!;
    }
  }

  Future<Database> initDb() async {
    final databasePath = await getDatabasesPath();
    final path = join(databasePath, "charactersDB.db");

    return await openDatabase(
      path,
      version: 1,
      onCreate: (Database db, int newVersion) async {
        await db.execute(
          "CREATE TABLE $characterTable("
          "$idColumn INTEGER PRIMARY KEY, "
          "$nameColumn TEXT, "
          "$imgColumn TEXT, "
          "$kindredColumn TEXT, "
          "$typeColumn TEXT, "
          "$levelColumn INTEGER, "
          "$strColumn INTEGER, "
          "$conColumn INTEGER, "
          "$dexColumn INTEGER, "
          "$spdColumn INTEGER, "
          "$lkColumn INTEGER, "
          "$iqColumn INTEGER, "
          "$wizColumn INTEGER, "
          "$chaColumn INTEGER, "
          "$equipColumn TEXT)",
        );
      },
    );
  }

  Future<Character> saveCharacter(Character character) async {
    Database dbSheet = await db;
    character.id = await dbSheet.insert(characterTable, character.toMap());
    return character;
  }

  Future<Character?> getCharacter(int id) async {
    Database dbSheet = await db;
    List<Map<String, dynamic>> maps = await dbSheet.query(
      characterTable,
      columns: [
        idColumn,
        nameColumn,
        imgColumn,
        kindredColumn,
        typeColumn,
        levelColumn,
        strColumn,
        conColumn,
        dexColumn,
        spdColumn,
        lkColumn,
        iqColumn,
        wizColumn,
        chaColumn,
        equipColumn,
      ],
      where: "$idColumn = ?",
      whereArgs: [id],
    );
    if (maps.isNotEmpty) {
      return Character.fromMap(maps.first);
    } else {
      return null;
    }
  }

  Future<List<Character>> getAllCharacters() async {
    Database dbSheet = await db;
    List<Map<String, dynamic>> listMap = await dbSheet.query(characterTable);
    List<Character> listCharacter = [];
    for (Map<String, dynamic> m in listMap) {
      listCharacter.add(Character.fromMap(m));
    }
    return listCharacter;
  }

  Future<int> deleteCharacter(int id) async {
    Database dbSheet = await db;
    return await dbSheet.delete(characterTable, where: "$idColumn = ?", whereArgs: [id]);
  }

  Future<int> updateCharacter(Character character) async {
    Database dbSheet = await db;
    return await dbSheet.update(
      characterTable,
      character.toMap(),
      where: "$idColumn = ?",
      whereArgs: [character.id],
    );
  }
}
