import 'package:apk_trabalho_1_dota/service/dota_service.dart';
import 'package:apk_trabalho_1_dota/view/hero_detail_page.dart';
import 'package:apk_trabalho_1_dota/widgets/role_chip.dart';
import 'package:flutter/material.dart';

enum OrderOptions { orderAZ, orderZA, orderWinRate, orderPickRate }

class HomePage extends StatefulWidget {
  const HomePage({super.key});

  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final DotaService dotaService = DotaService();
  final TextEditingController _searchController = TextEditingController();
  final _allHeroData = [];
  List _filteredHeroData = [];
  bool _isLoading = true;
  int _totalTurboPicks = 0;

  @override
  void initState() {
    super.initState();
    _loadHeroes();
  }

  void _loadHeroes() async {
    try {
      var heroes = await dotaService.getHeroes();
      for (var hero in heroes) {
        _totalTurboPicks += hero['turbo_picks'] as int;
      }
      for (var hero in heroes) {
        int turboWins = hero['turbo_wins'] as int;
        int turboPicks = hero['turbo_picks'] as int;
        hero['winRate'] = (turboPicks == 0) ? 0.0 : (turboWins / turboPicks);
        hero['pickRate'] = (_totalTurboPicks == 0) ? 0.0 : (turboPicks / _totalTurboPicks);
      }
      setState(() {
        _allHeroData.addAll(heroes);
        _filteredHeroData = _allHeroData;
        _isLoading = false;
      });
    } catch (e) {
      setState(() {
        _isLoading = false;
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(e.toString())));
      });
    }
  }

  void _filterHeroes(String query) {
    List<dynamic> results = [];
    if (query.isEmpty) {
      results = _allHeroData;
    } else {
      results = _allHeroData
          .where((hero) => hero['localized_name'].toLowerCase().contains(query.toLowerCase()))
          .toList();
    }
    setState(() {
      _filteredHeroData = results;
    });
  }

  void _orderList(OrderOptions result) {
    switch (result) {
      case OrderOptions.orderAZ:
        _filteredHeroData.sort((a, b) {
          return a['localized_name'].toLowerCase().compareTo(b['localized_name'].toLowerCase());
        });
        break;
      case OrderOptions.orderZA:
        _filteredHeroData.sort((a, b) {
          return b['localized_name'].toLowerCase().compareTo(a['localized_name'].toLowerCase());
        });
        break;
      case OrderOptions.orderWinRate:
        _filteredHeroData.sort((a, b) {
          return a['winRate'].compareTo(b['winRate']);
        });
        break;
      case OrderOptions.orderPickRate:
        _filteredHeroData.sort((a, b) {
          return b['pickRate'].compareTo(a['pickRate']);
        });
        break;
    }
    setState(() {});
  }

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        backgroundColor: Colors.black,
        title: Text("Dota 2", style: TextStyle(color: Colors.white)),
        centerTitle: true,
        actions: <Widget>[
          PopupMenuButton<OrderOptions>(
            icon: Icon(Icons.sort, color: Colors.white),
            color: Colors.grey[900],
            itemBuilder: (context) => <PopupMenuEntry<OrderOptions>>[
              const PopupMenuItem<OrderOptions>(
                value: OrderOptions.orderAZ,
                child: Text("Ordenar de A-Z", style: TextStyle(color: Colors.white)),
              ),
              const PopupMenuItem<OrderOptions>(
                value: OrderOptions.orderZA,
                child: Text("Ordenar de Z-A", style: TextStyle(color: Colors.white)),
              ),
              const PopupMenuItem<OrderOptions>(
                value: OrderOptions.orderWinRate,
                child: Text("Maior Win Rate", style: TextStyle(color: Colors.white)),
              ),
              const PopupMenuItem<OrderOptions>(
                value: OrderOptions.orderPickRate,
                child: Text("Maior Pick Rate", style: TextStyle(color: Colors.white)),
              ),
            ],
            onSelected: _orderList,
          ),
        ],
      ),
      backgroundColor: Colors.black,
      body: Column(
        children: <Widget>[
          Padding(
            padding: const EdgeInsets.all(10.0),
            child: TextField(
              controller: _searchController,
              onChanged: _filterHeroes,
              decoration: InputDecoration(
                labelText: "Pesquisar Herói",
                labelStyle: TextStyle(color: Colors.grey[400]),
                fillColor: Colors.grey[900],
                filled: true,
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(8.0),
                  borderSide: BorderSide.none,
                ),
                prefixIcon: Icon(Icons.search, color: Colors.grey[400]),
                suffixIcon: _searchController.text.isNotEmpty
                    ? IconButton(
                        icon: Icon(Icons.clear, color: Colors.grey[400]),
                        onPressed: () {
                          _searchController.clear();
                          _filterHeroes("");
                        },
                      )
                    : null,
              ),
              style: TextStyle(color: Colors.white),
            ),
          ),
          Expanded(child: _isLoading ? _loadingIndicator() : _createHeroList()),
        ],
      ),
    );
  }

  Widget _loadingIndicator() {
    return Center(
      child: CircularProgressIndicator(
        valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
        strokeWidth: 5.0,
      ),
    );
  }

  Widget _createHeroList() {
    final String baseImgUrl = "https://cdn.steamstatic.com";

    if (_filteredHeroData.isEmpty && !_isLoading) {
      return Center(
        child: Text(
          "Nenhum herói encontrado.",
          style: TextStyle(color: Colors.white, fontSize: 18),
        ),
      );
    }

    return ListView.builder(
      padding: EdgeInsets.all(10.0),
      itemCount: _filteredHeroData.length,
      itemBuilder: (context, index) {
        var hero = _filteredHeroData[index];
        double displayWinRate = (hero['winRate'] as double) * 100;
        double displayPickRate = (hero['pickRate'] as double) * 100;
        String heroIconUrl = baseImgUrl + hero["icon"];
        List<String> roles = List<String>.from(hero['roles'] ?? []);

        return GestureDetector(
          onTap: () {
            Navigator.push(context, MaterialPageRoute(builder: (context) => HeroDetailPage(hero)));
          },
          child: Card(
            color: Colors.grey[900],
            margin: EdgeInsets.symmetric(vertical: 8.0),
            child: Padding(
              padding: const EdgeInsets.all(12.0),
              child: Row(
                children: [
                  Container(
                    width: 60,
                    height: 60,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      image: DecorationImage(image: NetworkImage(heroIconUrl), fit: BoxFit.cover),
                    ),
                  ),
                  SizedBox(width: 15),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          crossAxisAlignment: CrossAxisAlignment.center,
                          children: [
                            Expanded(
                              child: Text(
                                hero['localized_name'],
                                style: TextStyle(
                                  color: Colors.white,
                                  fontSize: 18.0,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                            SizedBox(width: 10),
                            Column(
                              crossAxisAlignment: CrossAxisAlignment.end,
                              children: [
                                for (int i = 0; i < roles.length; i += 2)
                                  Padding(
                                    padding: EdgeInsets.only(top: i == 0 ? 0 : 4.0),
                                    child: Row(
                                      mainAxisAlignment: MainAxisAlignment.end,
                                      children: [
                                        roleChip(roles[i]),
                                        if (i + 1 < roles.length) ...[
                                          SizedBox(width: 6.0),
                                          roleChip(roles[i + 1]),
                                        ],
                                      ],
                                    ),
                                  ),
                              ],
                            ),
                          ],
                        ),
                        SizedBox(height: 8),
                        Text(
                          "Pick Rate: ${displayPickRate.toStringAsFixed(2)}% / Win Rate: ${displayWinRate.toStringAsFixed(2)}%",
                          style: TextStyle(color: Colors.grey[400], fontSize: 14.0),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ),
        );
      },
    );
  }
}
