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
aicent_bow = weapon("Ancient Bow", "Pierce", 32, 170)

class player1:
    def __init__(self, player_health, player_weapon1, player_weapon2, armor_head, armor_body):
        self.player_health = player_health
        self.player_weapon1 = player_weapon1
        self.player_weapon2 = player_weapon2
        self.armor_head = armor_head
        self.armor_body = armor_body

weapon1 = common_sword
weapon2 = common_bow
helm = common_armor_helm
armor = common_armor
player_health = 200

player = player1(player_health, weapon1, weapon2, helm, armor)


    

def upgrade():
    global weapon1
    global weapon2
    global helm
    global armor

    print("\nYou find loot on the body!")
    upgrade_catagory = random.randint(1,4)
    if upgrade_catagory == 1:
        if weapon1 == common_sword:
            weapon1 = uncommon_sword
            print("""Your "Common Sword" becomes a "Uncommon Sword"\n """)
        elif weapon1 == uncommon_sword:
            weapon1 = rare_sword
            print("""Your "Uncommon Sword" becomes a "Rare Sword"\n """)
        elif weapon1 == rare_sword:
            weapon1 = epic_sword
            print("""Your "Rare Sword" becomes a "Epic Sword"\n """)
        elif weapon1 == epic_sword:
            weapon1 = legendary_sword
            print("""Your "Epic Sword" becomes a "Legendary Sword"\n """)
        elif weapon1 == legendary_sword:
            weapon1 = relic_sword
            print("""Your "Legendary Sword" becomes a "Relic Sword"\n """)
        elif weapon1 == relic_sword:
            weapon1 = aicent_sword
            print("""Your "Relic Sword" becomes a "Ancient Sword"\n """)
    elif upgrade_catagory == 2:
        if weapon2 == common_bow:
            weapon2 = uncommon_sword
            print("""Your "Common Bow" becomes a "Uncommon Bow"\n """)
        elif weapon2 == uncommon_bow:
            weapon2 = rare_sword
            print("""Your "Uncommon Bow" becomes a "Rare Bow"\n """)
        elif weapon2 == rare_bow:
            weapon2 = epic_sword
            print("""Your "Rare Bow" becomes a "Epic Bow"\n """)
        elif weapon2 == epic_bow:
            weapon2 = legendary_bow
            print("""Your "Epic Bow" becomes a "Legendary Bow"\n """)
        elif weapon2 == legendary_bow:
            weapon2 = relic_bow
            print("""Your "Legendary Bow" becomes a "Relic Bow"\n """)
        elif weapon2 == relic_bow:
            weapon2 = aicent_bow
            print("""Your "Relic Bow" becomes a "Ancient Bow"\n """)
    elif upgrade_catagory == 3:
        if helm == common_armor_helm:
            helm = uncommon_armor_helm
            print("""Your "Common Helm" becomes a "Uncommon Helm"\n """)
        elif helm == uncommon_armor_helm:
            helm = rare_armor_helm
            print("""Your "Uncommon Helm" becomes a "Rare Helm"\n """)
        elif helm == rare_armor_helm:
            helm = epic_armor_helm
            print("""Your "Rare Helm" becomes a "Epic Helm"\n """)
        elif helm == epic_armor_helm:
            helm = legendary_armor_helm
            print("""Your "Epic Helm" becomes a "Legendary Helm"\n """)
        elif helm == legendary_armor_helm:
            helm = relic_armor_helm
            print("""Your "Legendary Helm" becomes a "Relic Helm"\n """)
        elif helm == relic_armor_helm:
            helm = aicent_armor_helm
            print("""Your "Relic Helm" becomes a "Ancient Helm"\n """)
    elif upgrade_catagory == 4:
        if armor == common_armor:
            armor = uncommon_armor
            print("""Your "Common Armor" becomes a "Uncommon Armor"\n """)
        elif armor == uncommon_armor:
            armor = rare_armor
            print("""Your "Uncommon Armor" becomes a "Rare Armor"\n """)
        elif armor == rare_armor:
            armor = epic_armor
            print("""Your "Rare Armor" becomes a "Epic Armor"\n """)
        elif armor == epic_armor:
            armor = legendary_armor
            print("""Your "Epic Armor" becomes a "Legendary Armor"\n """)
        elif armor == legendary_armor:
            armor = relic_armor
            print("""Your "Legendary Armor" becomes a "Relic Armor"\n """)
        elif armor == relic_armor:
            armor = aicent_armor
            print("""Your "Relic Armor" becomes a "Ancient Armor"\n """)