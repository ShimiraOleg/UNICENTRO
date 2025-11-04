import 'package:http/http.dart' as http;
import 'dart:convert';

class DotaService {
  List<Map<String, dynamic>> _heroCache = [];

  Future<void> _loadHeroes() async {
    if (_heroCache.isNotEmpty) {
      return;
    }
    final Uri url = Uri.parse("https://api.opendota.com/api/heroStats");
    http.Response response = await http.get(url);
    if (response.statusCode == 200) {
      final List<dynamic> rawList = json.decode(response.body);
      _heroCache = rawList.cast<Map<String, dynamic>>();
    } else {
      throw Exception('Falha ao carregar os dados da API');
    }
  }

  Future<List<Map<String, dynamic>>> listAllHeroes() async {
    await _loadHeroes();
    return _heroCache;
  }

  Future<Map<String, dynamic>?> getHeroByExactName(String name) async {
    await _loadHeroes();
    final String lowerCaseName = name.toLowerCase();

    try {
      return _heroCache.firstWhere(
        (hero) =>
            (hero['localized_name'] as String).toLowerCase() == lowerCaseName,
      );
    } catch (e) {
      return null;
    }
  }

  Future<List<Map<String, dynamic>>> filterHeroes({
    String? searchName,
    String? selectedAttribute,
    List<String>? selectedRoles,
  }) async {
    await _loadHeroes();

    Iterable<Map<String, dynamic>> results = _heroCache;

    if (selectedAttribute != null && selectedAttribute.isNotEmpty) {
      results = results.where((hero) {
        final String primaryAttr = (hero['primary_attr'] as String)
            .toLowerCase();
        return primaryAttr == selectedAttribute.toLowerCase();
      });
    }
    if (selectedRoles != null && selectedRoles.isNotEmpty) {
      results = results.where((hero) {
        final List<String> heroRoles = (hero['roles'] as List<dynamic>)
            .cast<String>()
            .map((role) => role.toLowerCase())
            .toList();
        return selectedRoles.every((selectedRole) {
          return heroRoles.contains(selectedRole.toLowerCase());
        });
      });
    }
    if (searchName != null && searchName.isNotEmpty) {
      final String lowerCaseQuery = searchName.toLowerCase();
      results = results.where((hero) {
        final String heroName = (hero['localized_name'] as String)
            .toLowerCase();
        return heroName.contains(lowerCaseQuery);
      });
    }
    return results.toList();
  }

  Future<List<String>> getAvailableRoles() async {
    await _loadHeroes();

    final allRolesSet = <String>{};
    for (var hero in _heroCache) {
      final List<String> heroRoles = (hero['roles'] as List<dynamic>)
          .cast<String>();
      allRolesSet.addAll(heroRoles);
    }

    final sortedList = allRolesSet.toList()..sort();
    return sortedList;
  }

  Future<List<String>> getAvailableAttributes() async {
    await _loadHeroes();

    final allAttrsSet = <String>{};
    for (var hero in _heroCache) {
      allAttrsSet.add(hero['primary_attr'] as String);
    }

    return allAttrsSet.toList();
  }
}
