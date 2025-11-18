import 'package:apk_trabalho_1_dota/service/dota_service.dart';
import 'package:apk_trabalho_1_dota/view/hero_detail_page.dart';
import 'package:apk_trabalho_1_dota/model/dota_hero.dart';
import 'package:apk_trabalho_1_dota/widgets/role_chip.dart';
import 'package:flutter/material.dart';

enum OrderOptions { orderAZ, orderZA, orderWinRate, orderPickRate }

extension OrderOptionsExtension on OrderOptions {
  String get displayName {
    switch (this) {
      case OrderOptions.orderAZ:
        return "A-Z";
      case OrderOptions.orderZA:
        return "Z-A";
      case OrderOptions.orderWinRate:
        return "Win Rate";
      case OrderOptions.orderPickRate:
        return "Pick Rate";
    }
  }
}

class HomePage extends StatefulWidget {
  const HomePage({super.key});
  @override
  State<HomePage> createState() => _HomePageState();
}

class _HomePageState extends State<HomePage> {
  final DotaService dotaService = DotaService();
  final TextEditingController _searchController = TextEditingController();
  final List<DotaHero> _allHeroData = [];
  List<DotaHero> _filteredHeroData = [];
  bool _isLoading = true;
  @override
  void initState() {
    super.initState();
    _loadHeroes();
  }

  void _loadHeroes() async {
    try {
      var heroes = await dotaService.getHeroes();
      setState(() {
        _allHeroData.addAll(heroes);
        _filteredHeroData = _allHeroData;
        _isLoading = false;
      });
    } catch (e) {
      setState(() {
        _isLoading = false;
        if (mounted) {
          ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(e.toString())));
        }
      });
    }
  }

  void _filterHeroes(String query) {
    List<DotaHero> results = [];
    if (query.isEmpty) {
      results = _allHeroData;
    } else {
      results = _allHeroData
          .where((hero) => hero.localizedName.toLowerCase().contains(query.toLowerCase()))
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
          return a.localizedName.toLowerCase().compareTo(b.localizedName.toLowerCase());
        });
        break;
      case OrderOptions.orderZA:
        _filteredHeroData.sort((a, b) {
          return b.localizedName.toLowerCase().compareTo(a.localizedName.toLowerCase());
        });
        break;
      case OrderOptions.orderWinRate:
        _filteredHeroData.sort((a, b) {
          return b.winRate.compareTo(a.winRate);
        });
        break;
      case OrderOptions.orderPickRate:
        _filteredHeroData.sort((a, b) {
          return b.pickRate.compareTo(a.pickRate);
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
        title: const Text("Dota 2", style: TextStyle(color: Colors.white)),
        centerTitle: true,
        actions: <Widget>[
          PopupMenuButton<OrderOptions>(
            icon: const Icon(Icons.sort, color: Colors.white),
            color: Colors.grey[900],
            itemBuilder: (context) => <PopupMenuEntry<OrderOptions>>[
              for (var option in OrderOptions.values)
                PopupMenuItem<OrderOptions>(
                  value: option,
                  child: Text(option.displayName, style: const TextStyle(color: Colors.white)),
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
              style: const TextStyle(color: Colors.white),
            ),
          ),
          Expanded(child: _isLoading ? _loadingIndicator() : _createHeroList()),
        ],
      ),
    );
  }

  Widget _loadingIndicator() {
    return const Center(
      child: CircularProgressIndicator(
        valueColor: AlwaysStoppedAnimation<Color>(Colors.white),
        strokeWidth: 5.0,
      ),
    );
  }

  Widget _createHeroList() {
    if (_filteredHeroData.isEmpty && !_isLoading) {
      return const Center(
        child: Text(
          "Nenhum herói encontrado.",
          style: TextStyle(color: Colors.white, fontSize: 18),
        ),
      );
    }

    return ListView.builder(
      padding: const EdgeInsets.all(10.0),
      itemCount: _filteredHeroData.length,
      itemBuilder: (context, index) {
        final hero = _filteredHeroData[index];
        double displayWinRate = hero.winRate * 100;
        double displayPickRate = hero.pickRate * 100;

        return GestureDetector(
          onTap: () {
            Navigator.push(context, MaterialPageRoute(builder: (context) => HeroDetailPage(hero)));
          },
          child: Card(
            color: Colors.grey[900],
            margin: const EdgeInsets.symmetric(vertical: 8.0),
            child: Padding(
              padding: const EdgeInsets.all(12.0),
              child: Row(
                children: [
                  Container(
                    width: 60,
                    height: 60,
                    decoration: BoxDecoration(
                      shape: BoxShape.circle,
                      image: DecorationImage(image: NetworkImage(hero.iconUrl), fit: BoxFit.cover),
                    ),
                  ),
                  const SizedBox(width: 15),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Row(
                          crossAxisAlignment: CrossAxisAlignment.center,
                          children: [
                            Expanded(
                              child: Text(
                                hero.localizedName,
                                style: const TextStyle(
                                  color: Colors.white,
                                  fontSize: 18.0,
                                  fontWeight: FontWeight.bold,
                                ),
                              ),
                            ),
                            const SizedBox(width: 10),
                            Column(
                              crossAxisAlignment: CrossAxisAlignment.end,
                              children: [
                                for (int i = 0; i < hero.roles.length; i += 2)
                                  Padding(
                                    padding: EdgeInsets.only(top: i == 0 ? 0 : 4.0),
                                    child: Row(
                                      mainAxisAlignment: MainAxisAlignment.end,
                                      children: [
                                        RoleChip(hero.roles[i]),
                                        if (i + 1 < hero.roles.length) ...[
                                          const SizedBox(width: 6.0),
                                          RoleChip(hero.roles[i + 1]),
                                        ],
                                      ],
                                    ),
                                  ),
                              ],
                            ),
                          ],
                        ),
                        const SizedBox(height: 8),
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
