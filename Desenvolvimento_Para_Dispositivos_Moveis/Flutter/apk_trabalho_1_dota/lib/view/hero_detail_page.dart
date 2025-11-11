import 'package:apk_trabalho_1_dota/widgets/image_text.dart';
import 'package:apk_trabalho_1_dota/widgets/role_chip.dart';
import 'package:apk_trabalho_1_dota/widgets/stat_bar.dart';
import 'package:flutter/material.dart';

class HeroDetailPage extends StatelessWidget {
  final Map _heroData;
  const HeroDetailPage(this._heroData, {super.key});
  final String _urlCharacter = "https://cdn.steamstatic.com";
  final String _urlIconsDota = "https://cdn.steamstatic.com/apps/dota2/images/dota_react/icons/";
  final String _urlIcons =
      "https://cdn.steamstatic.com/apps/dota2/images/dota_react//heroes/stats/";

  @override
  Widget build(BuildContext context) {
    List<String> roles = List<String>.from(_heroData['roles'] ?? []);
    String attribute = 'n/a';
    String iconAtk = _heroData['attack_type'] == 'Melee' ? 'melee.svg' : 'ranged.svg';
    String iconAttr = 'n/a';
    switch (_heroData['primary_attr'].toUpperCase()) {
      case 'AGI':
        attribute = 'Agilidade';
        iconAttr = 'hero_agility.png';
        break;
      case 'INT':
        attribute = 'Inteligência';
        iconAttr = 'hero_intelligence.png';
        break;
      case 'STR':
        attribute = 'Força';
        iconAttr = 'hero_strength.png';
        break;
      case 'ALL':
        attribute = 'Universal';
        iconAttr = 'hero_universal.png';
        break;
    }

    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          onPressed: () {
            Navigator.pop(context);
          },
          icon: Icon(Icons.arrow_back, color: Colors.white),
        ),
        backgroundColor: Colors.black,
        title: Text(_heroData["localized_name"], style: TextStyle(color: Colors.white)),
        centerTitle: true,
      ),
      backgroundColor: Colors.black,
      body: SingleChildScrollView(
        padding: EdgeInsets.all(16.0),
        child: Center(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Image.network(_urlCharacter + _heroData["img"]),
              SizedBox(height: 20),
              statBar(
                Colors.green,
                _heroData['base_health'].toString(),
                _heroData['base_health_regen'].toString(),
              ),
              statBar(
                Colors.blue,
                _heroData['base_mana'].toString(),
                _heroData['base_mana_regen'].toString(),
              ),
              SizedBox(height: 20),
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Expanded(
                    child: Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 8.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: <Widget>[
                          imageText(_urlIconsDota + iconAttr, attribute, 8.0),
                          imageText(_urlIconsDota + iconAtk, _heroData['attack_type'], 8.0),
                          SizedBox(height: 20),
                          for (int i = 0; i < roles.length; i++) ...[
                            roleChip(roles[i]),
                            if (i < roles.length - 1) SizedBox(height: 8.0),
                          ],
                          SizedBox(height: 20),
                          Text("Defesa", style: TextStyle(color: Colors.white, fontSize: 24)),
                          imageText(
                            '${_urlIcons}icon_armor.png',
                            _heroData['base_armor'].toString(),
                            2.0,
                          ),
                          imageText(
                            '${_urlIcons}icon_magic_resist.png',
                            "${_heroData['base_mr']}%",
                            2.0,
                          ),
                        ],
                      ),
                    ),
                  ),
                  Expanded(
                    child: Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 8.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: <Widget>[
                          imageText(
                            '${_urlIconsDota}hero_strength.png',
                            "${_heroData['base_str']}  +${_heroData['str_gain']}",
                            2.0,
                          ),
                          imageText(
                            '${_urlIconsDota}hero_agility.png',
                            "${_heroData['base_agi']}  +${_heroData['agi_gain']}",
                            2.0,
                          ),
                          imageText(
                            '${_urlIconsDota}hero_intelligence.png',
                            "${_heroData['base_int']}  +${_heroData['int_gain']}",
                            2.0,
                          ),
                          SizedBox(height: 20),
                          Text("Ataque", style: TextStyle(color: Colors.white, fontSize: 24)),
                          imageText(
                            '${_urlIcons}icon_damage.png',
                            "${_heroData['base_attack_min']}-${_heroData['base_attack_max']}",
                            2.0,
                          ),
                          imageText(
                            '${_urlIcons}icon_attack_time.png',
                            _heroData['attack_rate'].toString(),
                            2.0,
                          ),
                          imageText(
                            '${_urlIcons}icon_attack_range.png',
                            _heroData['attack_range'].toString(),
                            2.0,
                          ),
                          _heroData['projectile_speed'] != 0
                              ? imageText(
                                  '${_urlIcons}icon_projectile_speed.png',
                                  _heroData['projectile_speed'].toString(),
                                  2.0,
                                )
                              : SizedBox(),
                          SizedBox(height: 20),
                          Text("Movimentação", style: TextStyle(color: Colors.white, fontSize: 24)),
                          imageText(
                            '${_urlIcons}icon_movement_speed.png',
                            _heroData['move_speed'].toString(),
                            2.0,
                          ),
                          _heroData['turn_rate'] != null
                              ? imageText(
                                  '${_urlIcons}icon_turn_rate.png',
                                  _heroData['turn_rate'].toString(),
                                  2.0,
                                )
                              : SizedBox(),
                          imageText(
                            '${_urlIcons}icon_vision.png',
                            '${_heroData['day_vision']}/${_heroData["night_vision"]}',
                            2.0,
                          ),
                        ],
                      ),
                    ),
                  ),
                ],
              ),
            ],
          ),
        ),
      ),
    );
  }
}
