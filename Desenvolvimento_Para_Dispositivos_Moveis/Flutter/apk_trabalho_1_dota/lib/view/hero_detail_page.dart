import 'package:apk_trabalho_1_dota/app_constraints.dart';
import 'package:apk_trabalho_1_dota/model/dota_hero.dart';
import 'package:apk_trabalho_1_dota/widgets/image_text.dart';
import 'package:apk_trabalho_1_dota/widgets/role_chip.dart';
import 'package:apk_trabalho_1_dota/widgets/stat_bar.dart';
import 'package:flutter/material.dart';

class HeroDetailPage extends StatelessWidget {
  final DotaHero heroData;
  const HeroDetailPage(this.heroData, {super.key});

  @override
  Widget build(BuildContext context) {
    String attribute = heroData.primaryAttributeText;
    String iconAttr = heroData.primaryAttributeIconUrl;
    String iconAtk = heroData.attackTypeIconUrl;

    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
          onPressed: () {
            Navigator.pop(context);
          },
          icon: const Icon(Icons.arrow_back, color: Colors.white),
        ),
        backgroundColor: Colors.black,
        title: Text(heroData.localizedName, style: const TextStyle(color: Colors.white)),
        centerTitle: true,
      ),
      backgroundColor: Colors.black,
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Center(
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.center,
            children: [
              Image.network(heroData.imgUrl),
              const SizedBox(height: 20),
              StatBar(
                barColor: Colors.green,
                baseValue: heroData.baseHealth.toString(),
                gainValue: heroData.baseHealthRegen.toStringAsFixed(1),
              ),
              StatBar(
                barColor: Colors.blue,
                baseValue: heroData.baseMana.toString(),
                gainValue: heroData.baseManaRegen.toStringAsFixed(1),
              ),
              const SizedBox(height: 20),
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Expanded(
                    child: Padding(
                      padding: const EdgeInsets.symmetric(horizontal: 8.0),
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: <Widget>[
                          ImageText(url: iconAttr, text: attribute, space: 8.0),
                          ImageText(url: iconAtk, text: heroData.attackType, space: 8.0),
                          const SizedBox(height: 20),
                          for (int i = 0; i < heroData.roles.length; i++) ...[
                            RoleChip(heroData.roles[i]),
                            if (i < heroData.roles.length - 1) const SizedBox(height: 8.0),
                          ],
                          const SizedBox(height: 20),
                          const Text("Defesa", style: TextStyle(color: Colors.white, fontSize: 24)),
                          ImageText(
                            url: AppConstants.iconArmor,
                            text: heroData.baseArmor.toStringAsFixed(1),
                            space: 2.0,
                          ),
                          ImageText(
                            url: AppConstants.iconMagicResist,
                            text: "${heroData.baseMr}%",
                            space: 2.0,
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
                          ImageText(
                            url: AppConstants.iconAttrStrength,
                            text: "${heroData.baseStr}  +${heroData.strGain}",
                            space: 2.0,
                          ),
                          ImageText(
                            url: AppConstants.iconAttrAgility,
                            text: "${heroData.baseAgi}  +${heroData.agiGain}",
                            space: 2.0,
                          ),
                          ImageText(
                            url: AppConstants.iconAttrIntelligence,
                            text: "${heroData.baseInt}  +${heroData.intGain}",
                            space: 2.0,
                          ),
                          const SizedBox(height: 20),
                          const Text("Ataque", style: TextStyle(color: Colors.white, fontSize: 24)),
                          ImageText(
                            url: AppConstants.iconDamage,
                            text: "${heroData.baseAttackMin}-${heroData.baseAttackMax}",
                            space: 2.0,
                          ),
                          ImageText(
                            url: AppConstants.iconAttackTime,
                            text: heroData.attackRate.toString(),
                            space: 2.0,
                          ),
                          ImageText(
                            url: AppConstants.iconAttackRange,
                            text: heroData.attackRange.toString(),
                            space: 2.0,
                          ),
                          if (heroData.projectileSpeed != 0)
                            ImageText(
                              url: AppConstants.iconProjectileSpeed,
                              text: heroData.projectileSpeed.toString(),
                              space: 2.0,
                            ),
                          const SizedBox(height: 20),
                          const Text(
                            "Movimentação",
                            style: TextStyle(color: Colors.white, fontSize: 24),
                          ),
                          ImageText(
                            url: AppConstants.iconMovementSpeed,
                            text: heroData.moveSpeed.toString(),
                            space: 2.0,
                          ),
                          if (heroData.turnRate != null)
                            ImageText(
                              url: AppConstants.iconTurnRate,
                              text: heroData.turnRate.toString(),
                              space: 2.0,
                            ),
                          ImageText(
                            url: AppConstants.iconVision,
                            text: '${heroData.dayVision}/${heroData.nightVision}',
                            space: 2.0,
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
