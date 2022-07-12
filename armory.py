import random
class armor_body:
    def __init__(self, armor_body_name, dmg_reduction, cost):
        self.armor_body_name = armor_body_name
        self.dmg_reduction = dmg_reduction
        self.cost = cost
        
common_armor = armor_body("Common Armor", 2, 50)
uncommon_armor = armor_body("Uncommon Armor", 4, 70)
rare_armor = armor_body("Rare Armor", 6, 90)
epic_armor = armor_body("Epic Armor", 8, 110)
legendary_armor = armor_body("Legendary Armor", 10, 130)
relic_armor = armor_body("Relic Armor", 12, 150)
aicent_armor = armor_body("Ancient Armor", 14, 170)

class armor_helm:
    def __init__(self, armor_helm_name, dmg_reduction, cost):
        self.armor_helm_name = armor_helm_name
        self.dmg_reduction = dmg_reduction
        self.cost = cost
        
common_armor_helm = armor_helm("Common Helm", 1, 25)
uncommon_armor_helm = armor_helm("Uncommon Helm", 2, 35)
rare_armor_helm = armor_helm("Rare Helm", 3, 45)
epic_armor_helm = armor_helm("Epic Helm", 4, 55)
legendary_armor_helm = armor_helm("Legendary Helm", 5, 65)
relic_armor_helm = armor_helm("Relic Helm", 6, 75)
aicent_armor_helm = armor_helm("Ancient Helm", 7, 85)

class weapon:
    def __init__(self, weapon_name, weapon_dmg_type, weapon_dmg, cost):
        self.weapon_name = weapon_name
        self.weapon_dmg_type = weapon_dmg_type
        self.weapon_dmg = weapon_dmg
        self.cost = cost 
        
common_sword = weapon("common sword", "Slash", 8, 50)
uncommon_sword = weapon("uncommon sword", "Slash", 12, 70)
rare_sword = weapon("rare sword", "Slash", 16, 90)
epic_sword = weapon("epic sword", "Slash", 20, 110)
legendary_sword = weapon("legendary sword", "Slash", 24, 130)
relic_sword = weapon("relic sword", "Slash", 28, 150)
aicent_sword = weapon("ancient sword", "Slash", 32, 170)

common_hammer = weapon("Common Hammer", "Blunt", 8, 50)
uncommon_hammer = weapon("Uncommon Hammer", "Blunt", 12, 70)
rare_hammer = weapon("Rare Hammer", "Blunt", 16, 90)
epic_hammer = weapon("Epic Hammer", "Blunt", 20, 110)
legendary_hammer = weapon("Legendary Hammer", "Blunt", 24, 130)
relic_hammer = weapon("Relic Hammer", "Blunt", 28, 150)
aicent_hammer = weapon("Ancient Hammer", "Blunt", 32, 170)

common_bow = weapon("common bow", "Pierce", 8, 50)
uncommon_bow = weapon("uncommon bow", "Pierce", 12, 70)
rare_bow = weapon("rare bow", "Pierce", 16, 90)
epic_bow = weapon("epic bow", "Pierce", 20, 110)
legendary_bow= weapon("legendary bow", "Pierce", 24, 130)
relic_bow = weapon("relic bow", "pierce", 28, 150)
aicent_bow = weapon("ancient Bow", "Pierce", 32, 170)

