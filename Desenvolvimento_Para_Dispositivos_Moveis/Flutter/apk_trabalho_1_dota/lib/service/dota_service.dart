import 'dart:convert';
import 'package:http/http.dart' as http;

class DotaService {
  final String _apiUrl = "https://api.opendota.com/api/heroStats";

  Future<List> getHeroes() async {
    http.Response response = await http.get(Uri.parse(_apiUrl));

    if (response.statusCode == 200) {
      return json.decode(response.body);
    } else {
      throw Exception('Falha ao carregar os dados dos heróis');
    }
  }
}
