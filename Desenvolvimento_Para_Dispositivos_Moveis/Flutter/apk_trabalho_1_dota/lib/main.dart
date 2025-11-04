import 'package:flutter/material.dart';
import 'dota_service.dart';

Future<void> main() async {
  runApp(const Placeholder());
  DotaService ds = DotaService();
  List<Map<String, dynamic>> heroi = await ds.listAllHeroes();
  // Exemplo 1: Pegar todos os heróis de "str" (Força)
  List<Map<String, dynamic>> strHeroes = await ds.filterHeroes(
    selectedAttribute: "str",
  );

  // Exemplo 2: Pegar todos os heróis que são "Support"
  List<Map<String, dynamic>> supports = await ds.filterHeroes(
    selectedRoles: ["Support"],
  );

  // Exemplo 3: Pegar heróis que são "Carry" E "Disabler"
  List<Map<String, dynamic>> carryDisablers = await ds.filterHeroes(
    selectedRoles: ["Carry", "Disabler"],
  );

  // Exemplo 4 (Corrigido): Pegar heróis "agi" que tenham "mage" no nome
  List<Map<String, dynamic>> agiMages = await ds.filterHeroes(
    selectedAttribute: "agi",
    searchName: "Mage", // (Isso deve retornar o "Anti-Mage")
  );
  print("\n");
  print(agiMages);

  // Exemplo 5 (COMBINADO): Herói de "str", que seja "Initiator" e tenha "king" no nome
  List<Map<String, dynamic>> complexSearch = await ds.filterHeroes(
    selectedAttribute: "str",
    selectedRoles: ["Initiator"],
    searchName: "king",
    // (Isso pode retornar "Wraith King" e "Sand King", se ele for str e initiator)
  );
}
