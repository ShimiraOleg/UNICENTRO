import 'package:apk_trabalho_1_dota/app_constraints.dart';

class DotaHero {
  final int id;
  final String name;
  final String localizedName;
  final String primaryAttr;
  final String attackType;
  final List<String> roles;
  final String img;
  final String icon;
  final int baseHealth;
  final double baseHealthRegen;
  final int baseMana;
  final double baseManaRegen;
  final double baseArmor;
  final int baseMr;
  final int baseStr;
  final double strGain;
  final int baseAgi;
  final double agiGain;
  final int baseInt;
  final double intGain;
  final int baseAttackMin;
  final int baseAttackMax;
  final double attackRate;
  final int attackRange;
  final int projectileSpeed;
  final int moveSpeed;
  final double? turnRate;
  final int dayVision;
  final int nightVision;
  final double winRate;
  final double pickRate;

  DotaHero({
    required this.id,
    required this.name,
    required this.localizedName,
    required this.primaryAttr,
    required this.attackType,
    required this.roles,
    required this.img,
    required this.icon,
    required this.baseHealth,
    required this.baseHealthRegen,
    required this.baseMana,
    required this.baseManaRegen,
    required this.baseArmor,
    required this.baseMr,
    required this.baseStr,
    required this.strGain,
    required this.baseAgi,
    required this.agiGain,
    required this.baseInt,
    required this.intGain,
    required this.baseAttackMin,
    required this.baseAttackMax,
    required this.attackRate,
    required this.attackRange,
    required this.projectileSpeed,
    required this.moveSpeed,
    this.turnRate,
    required this.dayVision,
    required this.nightVision,
    required this.winRate,
    required this.pickRate,
  });
  factory DotaHero.fromJson(Map<String, dynamic> json, int totalTurboPicks) {
    int turboPicks = json['turbo_picks'] as int;
    int turboWins = json['turbo_wins'] as int;
    double calculatedWinRate = (turboPicks == 0) ? 0.0 : (turboWins / turboPicks);
    double calculatedPickRate = (totalTurboPicks == 0) ? 0.0 : (turboPicks / totalTurboPicks);

    return DotaHero(
      id: json['id'] as int,
      name: json['name'] as String,
      localizedName: json['localized_name'] as String,
      primaryAttr: json['primary_attr'] as String,
      attackType: json['attack_type'] as String,
      roles: List<String>.from(json['roles'] ?? []),
      img: json['img'] as String,
      icon: json['icon'] as String,
      baseHealth: json['base_health'] as int,
      baseHealthRegen: (json['base_health_regen'] as num?)?.toDouble() ?? 0.0,
      baseMana: json['base_mana'] as int,
      baseManaRegen: (json['base_mana_regen'] as num?)?.toDouble() ?? 0.0,
      baseArmor: (json['base_armor'] as num?)?.toDouble() ?? 0.0,
      baseMr: json['base_mr'] as int,
      baseStr: json['base_str'] as int,
      strGain: (json['str_gain'] as num?)?.toDouble() ?? 0.0,
      baseAgi: json['base_agi'] as int,
      agiGain: (json['agi_gain'] as num?)?.toDouble() ?? 0.0,
      baseInt: json['base_int'] as int,
      intGain: (json['int_gain'] as num?)?.toDouble() ?? 0.0,
      baseAttackMin: json['base_attack_min'] as int,
      baseAttackMax: json['base_attack_max'] as int,
      attackRate: (json['attack_rate'] as num?)?.toDouble() ?? 0.0,
      attackRange: json['attack_range'] as int,
      projectileSpeed: json['projectile_speed'] as int,
      moveSpeed: json['move_speed'] as int,
      turnRate: (json['turn_rate'] as num?)?.toDouble(),
      dayVision: json['day_vision'] as int,
      nightVision: json['night_vision'] as int,
      winRate: calculatedWinRate,
      pickRate: calculatedPickRate,
    );
  }

  String get iconUrl => AppConstants.baseSteamUrl + icon;
  String get imgUrl => AppConstants.baseSteamUrl + img;

  String get primaryAttributeText {
    switch (primaryAttr.toUpperCase()) {
      case 'AGI':
        return 'Agilidade';
      case 'INT':
        return 'Inteligência';
      case 'STR':
        return 'Força';
      case 'ALL':
        return 'Universal';
      default:
        return 'n/a';
    }
  }

  String get primaryAttributeIconUrl {
    switch (primaryAttr.toUpperCase()) {
      case 'AGI':
        return AppConstants.iconAttrAgility;
      case 'INT':
        return AppConstants.iconAttrIntelligence;
      case 'STR':
        return AppConstants.iconAttrStrength;
      case 'ALL':
        return AppConstants.iconAttrUniversal;
      default:
        return '';
    }
  }

  String get attackTypeIconUrl {
    return attackType == 'Melee' ? AppConstants.iconAttackMelee : AppConstants.iconAttackRanged;
  }
}
