import 'dart:convert';
import 'package:apk_trabalho_1_dota/app_constraints.dart';
import 'package:apk_trabalho_1_dota/model/dota_hero.dart';
import 'package:http/http.dart' as http;

class DotaService {
  Future<List<DotaHero>> getHeroes() async {
    http.Response response = await http.get(Uri.parse(AppConstants.baseApiUrl));

    if (response.statusCode == 200) {
      List<dynamic> rawData = json.decode(response.body);
      int totalTurboPicks = 0;
      for (var heroJson in rawData) {
        totalTurboPicks += (heroJson['turbo_picks'] as int? ?? 0);
      }
      List<DotaHero> heroes = rawData.map((heroJson) {
        return DotaHero.fromJson(heroJson, totalTurboPicks);
      }).toList();
      return heroes;
    } else {
      throw Exception('Falha ao carregar os dados dos heróis');
    }
  }
}
