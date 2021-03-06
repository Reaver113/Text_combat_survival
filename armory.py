class ArmorBody:
    def __init__(self, armor_body_name, dmg_reduction, cost):
        self.armor_body_name = armor_body_name
        self.dmg_reduction = dmg_reduction
        self.cost = cost
        
common_armor = ArmorBody("Common Armor", 2, 50)
uncommon_armor = ArmorBody("Uncommon Armor", 4, 70)
rare_armor = ArmorBody("Rare Armor", 6, 90)
epic_armor = ArmorBody("Epic Armor", 8, 110)
legendary_armor = ArmorBody("Legendary Armor", 10, 130)
relic_armor = ArmorBody("Relic Armor", 12, 150)
aicent_armor = ArmorBody("Ancient Armor", 14, 170)

class ArmorHelm:
    def __init__(self, armor_helm_name, dmg_reduction, cost):
        self.armor_helm_name = armor_helm_name
        self.dmg_reduction = dmg_reduction
        self.cost = cost
        
common_armor_helm = ArmorHelm("Common Helm", 1, 25)
uncommon_armor_helm = ArmorHelm("Uncommon Helm", 2, 35)
rare_armor_helm = ArmorHelm("Rare Helm", 3, 45)
epic_armor_helm = ArmorHelm("Epic Helm", 4, 55)
legendary_armor_helm = ArmorHelm("Legendary Helm", 5, 65)
relic_armor_helm = ArmorHelm("Relic Helm", 6, 75)
aicent_armor_helm = ArmorHelm("Ancient Helm", 7, 85)

class Weapon:
    def __init__(self, weapon_name, weapon_dmg_type, weapon_dmg, cost):
        self.weapon_name = weapon_name
        self.weapon_dmg_type = weapon_dmg_type
        self.weapon_dmg = weapon_dmg
        self.cost = cost 
        
common_sword = Weapon("common sword", "Slash", 8, 50)
uncommon_sword = Weapon("uncommon sword", "Slash", 12, 70)
rare_sword = Weapon("rare sword", "Slash", 16, 90)
epic_sword = Weapon("epic sword", "Slash", 20, 110)
legendary_sword = Weapon("legendary sword", "Slash", 24, 130)
relic_sword = Weapon("relic sword", "Slash", 28, 150)
aicent_sword = Weapon("ancient sword", "Slash", 32, 170)

common_bow = Weapon("common bow", "Pierce", 8, 50)
uncommon_bow = Weapon("uncommon bow", "Pierce", 12, 70)
rare_bow = Weapon("rare bow", "Pierce", 16, 90)
epic_bow = Weapon("epic bow", "Pierce", 20, 110)
legendary_bow= Weapon("legendary bow", "Pierce", 24, 130)
relic_bow = Weapon("relic bow", "pierce", 28, 150)
aicent_bow = Weapon("ancient Bow", "Pierce", 32, 170)

