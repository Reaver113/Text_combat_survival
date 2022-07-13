import random
import shelve
from armory import *
from monsters import *

current_enemy_health_g = 0
enemy_1 = ""
enemy_2 = ""
enemy_3 = ""
enemy_4 = ""
current_foe = 0
current_enemy = ""
has_played = False
round_count = 0
dragon_count = 0
weapon1 = common_sword
weapon2 = common_bow
armor = common_armor
helm = common_armor_helm
player_health = 400
plyaer_name = ""

def run_preperation():
    global current_enemy
    global enemy_1
    global enemy_2
    global enemy_3
    global enemy_4
    global current_enemy_health_g
    global player_name

    enemy_roll1 = random.randint(1,5)

    if enemy_roll1 == 1:
        enemy1 = goblin
    elif enemy_roll1 == 2:
        enemy1 = rock_monster
    elif enemy_roll1 == 3:
        enemy1 = cyclops
    elif enemy_roll1 == 4:
        enemy1 = treeant
    elif enemy_roll1 == 5:
        enemy1 = orc

    enemy_roll2 = random.randint(1,5)


    if enemy_roll2 == 1:
        enemy2 = goblin
    elif enemy_roll2 == 2:
        enemy2 = rock_monster
    elif enemy_roll2 == 3:
        enemy2 = cyclops
    elif enemy_roll2 == 4:
        enemy2 = treeant
    elif enemy_roll2 == 5:
        enemy2 = orc

    enemy_roll3 = random.randint(1,5)



    if enemy_roll3 == 1:
        enemy3 = goblin
    elif enemy_roll3 == 2:
        enemy3 = rock_monster
    elif enemy_roll3 == 3:
        enemy3 = cyclops
    elif enemy_roll3 == 4:
        enemy3 = treeant
    elif enemy_roll3 == 5:
        enemy3 = orc

    enemy_roll4 = random.randint(1,5)


    if enemy_roll4 == 1:
        enemy4 = goblin
    elif enemy_roll4 == 2:
        enemy4 = rock_monster
    elif enemy_roll4 == 3:
        enemy4 = cyclops
    elif enemy_roll4 == 4:
        enemy4 = treeant
    elif enemy_roll4 == 5:
        enemy4 = orc

    user_ready = "not ready"

    player_name = input("Please enter your name: ")
    print(f"\nwelcome {player_name}")
    
    print("This rounds gauntlet will be!\n")
    print(enemy1.name)
    print(f"This enemy has {enemy1.health} Health, and is weak to {enemy1.weakness1} damage\n ")
    print("followed by:\n")
    print(enemy2.name)
    print(f"This enemy has {enemy2.health} Health, and is weak to {enemy2.weakness1} damage\n")
    print("followed by:\n")
    print(enemy3.name)
    print(f"This enemy has {enemy3.health} Health, and is weak to {enemy3.weakness1} damage\n")
    print("followed by:\n")
    print(enemy4.name )
    print(f"This enemy has {enemy4.health} Health, and is weak to {enemy4.weakness1} damage\n")
    print("Goodluck.... you're gonna need it....")

    while user_ready != "ready":
        user_ready = input("""Type "ready" to begin the challenge or "exit" to run: """)
        if user_ready == "ready":
            current_enemy_health_g = enemy1.health
            enemy_1 = enemy1
            enemy_2 = enemy2
            enemy_3 = enemy3
            enemy_4 = enemy4
            current_enemy = enemy_1
            round1()
            return
        if user_ready == "exit":
            exit()




def round1():
    global round_count
    global has_played
    global player_name
    action = ""
    if current_enemy == dragon_boss:
        print("THE MIGHTY DRAGON ROARS!!!!! This be a tough fight")
    elif has_played == False:
        print(f"\nYou stand before the {current_enemy.name} and prepare yourself.\n")
        has_played = True
    elif has_played == True:
        print(f"The {current_enemy.name} matches you gaze once more")


    while action != "quick attack"  or "heavy attack":
        action = input(""""Quick Attack"    "Heavy Attack"       "Stats"        "Scoreboard"      """).lower()
        if action == "quick":
            action = "quick attack"
        if action == "heavy":
            action = "heavy attack"

        if action == "quick attack":
            quick_attack()
            if current_enemy_health_g < 1:
                print(f"You have slain the {current_enemy.name}")
                has_played = False
                upgrade()
                round_reset()
            monster_attack()
            if player_health < 1:
                print("You have been defeated\n")
                score = shelve.open("highscore")
                score["Name"] = player_name
                score["Round Count"] = round_count
                score["Dragon Count"] = dragon_count
                for key in score:
                    print(score[key])
                score.close()
                print("\nYour score has been saved, Thank you for playing!")
                exit()
            else:
                round1()

        elif action == "heavy attack":
            heavy_attack()
            if current_enemy_health_g < 1:
                print(f"You have slain the {current_enemy.name}")
                has_played = False
                upgrade()
                round_reset()
                return
            monster_attack()
            if player_health < 1:
                print("You have been defeated")
                return
            else:
                round1()
        elif action == "stats":
            stats()
        elif action == "scoreboard":
            scoreboard()
        elif action == "quit":
            score = shelve.open("highscore")
            score["Name"] = player_name
            score["Round Count"] = round_count
            score["Dragon Count"] = dragon_count
            for key in score:
                print(score[key])
            score.close()
            print("\nYour score has been saved, Thank you for playing!")
            exit()


def scoreboard():
    score = shelve.open("highscore")
    print("\nName:")
    print(score["Name"])
    print("Rounds Passed:")
    print(score["Round Count"])
    print("Dragons Slain:")
    print(score["Dragon Count"])
    print("\n")
    score.close()


def quick_attack():
    global current_enemy_health_g
    chosen_weapon = "not chosen"
    while chosen_weapon != weapon1.weapon_name or weapon2.weapon_name:
        chosen_weapon = input(f"\nUse your {weapon1.weapon_name} or {weapon2.weapon_name}: ").lower()
        if chosen_weapon == "sword":
            chosen_weapon = weapon1.weapon_name
        if chosen_weapon == "bow":
            chosen_weapon = weapon2.weapon_name

        if chosen_weapon == weapon1.weapon_name :
            print(f"You attack with your {weapon1.weapon_name}\n")
            hit_chance = random.randint(1,100)
            if hit_chance > 25 and weapon1.weapon_dmg_type == current_enemy.weakness1:
                print(f"It Hits! ({weapon1.weapon_dmg}) + ({weapon1.weapon_dmg / 4} Weakness bonus)")
                current_enemy_health_g = current_enemy_health_g - ((weapon1.weapon_dmg / 4) + weapon1.weapon_dmg)
                print(f"The {current_enemy.name} has {current_enemy_health_g} HP remaing\n")
                return
            elif hit_chance > 25:
                print(f"It Hits! ({weapon1.weapon_dmg})")
                current_enemy_health_g = current_enemy_health_g - weapon1.weapon_dmg
                print(f"The {current_enemy.name} has {current_enemy_health_g} HP remaing\n")
                return
            else:
                print("Your attack misses\n")
                return
        if chosen_weapon == weapon2.weapon_name:
            print(f"You attack with your {weapon2.weapon_name}\n")
            hit_chance = random.randint(1,100)
            if hit_chance > 25 and weapon2.weapon_dmg_type == current_enemy.weakness1:
                print(f"It Hits! ({weapon2.weapon_dmg}) + ({weapon2.weapon_dmg / 4} Weakness bonus)")
                current_enemy_health_g = current_enemy_health_g - ((weapon2.weapon_dmg / 4) + weapon2.weapon_dmg)
                print(f"The {current_enemy.name} has {current_enemy_health_g} HP remaing\n")
                return
            elif hit_chance > 25:
                print(f"It Hits! ({weapon2.weapon_dmg})")
                current_enemy_health_g = current_enemy_health_g - weapon2.weapon_dmg
                print(f"The {current_enemy.name} has {current_enemy_health_g} HP remaing\n")
                return
            else:
                print("Your attack misses\n")
                return





def heavy_attack():
    global current_enemy_health_g
    chosen_weapon = "not chosen"
    while chosen_weapon != weapon1.weapon_name or weapon2.weapon_name:
        chosen_weapon = input(f"\nUse your {weapon1.weapon_name} or {weapon2.weapon_name}: ").lower()
        if chosen_weapon == "sword":
            chosen_weapon = weapon1.weapon_name
        if chosen_weapon == "bow":
            chosen_weapon = weapon2.weapon_name

        if chosen_weapon == weapon1.weapon_name:
            print(f"You attack with your {weapon1.weapon_name}\n")
            hit_chance = random.randint(1,100)
            if hit_chance > 45 and weapon1.weapon_dmg_type == current_enemy.weakness1:
                print(f"It Hits! ({weapon1.weapon_dmg}) + ({weapon1.weapon_dmg / 4} Weakness bonus) + ({weapon1.weapon_dmg / 2} + Heavy bonus)")
                current_enemy_health_g = current_enemy_health_g - ((weapon1.weapon_dmg / 4) +(weapon1.weapon_dmg / 2)+ weapon1.weapon_dmg)
                return
            elif hit_chance > 45:
                print(f"It Hits! ({weapon1.weapon_dmg}) + ({weapon1.weapon_dmg / 2} Heavy bonus)")
                current_enemy_health_g = current_enemy_health_g - ((weapon1.weapon_dmg / 2) + weapon1.weapon_dmg)
                print(f"The {current_enemy.name} has {current_enemy_health_g} HP remaing\n")
                return
            else:
                print("Your attack misses\n")
                return
        if chosen_weapon == weapon2.weapon_name:
            print(f"You attack with your {weapon2.weapon_name}\n")
            hit_chance = random.randint(1,100)
            if hit_chance > 45 and weapon2.weapon_dmg_type == current_enemy.weakness1:
                print(f"It Hits! ({weapon2.weapon_dmg}) + ({weapon2.weapon_dmg / 4} Weakness bonus) + ({weapon2.weapon_dmg / 2} + Heavy bonus)")
                current_enemy_health_g = current_enemy_health_g - ((weapon2.weapon_dmg / 4) +(weapon2.weapon_dmg / 2)+ weapon2.weapon_dmg)
                return
            if hit_chance > 45:
                print(f"It Hits! ({weapon2.weapon_dmg}) + heavy bonus ({weapon2.weapon_dmg / 2})")
                current_enemy_health_g = current_enemy_health_g - ((weapon2.weapon_dmg / 2) + weapon2.weapon_dmg)
                print(f"The {current_enemy.name} has {current_enemy_health_g} HP remaing\n")
                return
            else:
                print("Your attack misses\n")
                return






def monster_attack():
    global player_health
    if current_enemy == dragon_boss:
        monster_dmg_pre = random.randint(10, 20)
        monster_dmg = monster_dmg_pre + (monster_dmg_pre / 2) - helm.dmg_reduction - armor.dmg_reduction
        player_health = player_health - monster_dmg
        print(f"The {current_enemy.name} Hits you back for {monster_dmg} ({monster_dmg_pre} + {monster_dmg_pre / 2}) - {helm.dmg_reduction + armor.dmg_reduction} from armor stats)")
        print(f"You have {player_health} remaing\n")
    if current_enemy != dragon_boss:
        monster_dmg_pre = random.randint(10, 20)
        monster_dmg = monster_dmg_pre - helm.dmg_reduction - armor.dmg_reduction
        player_health = player_health - monster_dmg
        print(f"The {current_enemy.name} Hits you back for {monster_dmg} ({monster_dmg_pre} - {helm.dmg_reduction + armor.dmg_reduction} from armor stats)")
        print(f"You have {player_health} remaing\n")



def stats():
    print(f"\nYou current weild a {weapon1.weapon_name} ({weapon1.weapon_dmg} Damage) and a {weapon2.weapon_name} ({weapon2.weapon_dmg} Damage)")
    print(f"You have donned the {helm.armor_helm_name} ({helm.dmg_reduction} Defence) and {armor.armor_body_name} ({armor.dmg_reduction} Defence)") 
    print(f"You have sucessfully defeated {round_count} enimies and {dragon_count} Dragons\n")

def round_reset():
    global round_count
    global dragon_count
    global current_enemy
    global enemy_1
    global enemy_2
    global enemy_3
    global enemy_4
    global current_enemy_health_g

    if current_enemy == enemy_1:
        current_enemy = enemy_2
        round_count += 1
        current_enemy_health_g = current_enemy.health
        round1()
    elif current_enemy == enemy_2:
        current_enemy = enemy_3
        round_count += 1
        current_enemy_health_g = current_enemy.health
        round1()
    elif current_enemy == enemy_3:
        current_enemy = enemy_4
        round_count += 1
        current_enemy_health_g = current_enemy.health
        round1()
    elif current_enemy == enemy_4:
        current_enemy = dragon_boss
        round_count += 1
        current_enemy_health_g = current_enemy.health
        round1()
    elif current_enemy == dragon_boss:
        dragon_count += 1
        run_preperation()

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
            weapon2 = uncommon_bow
            print("""Your "Common Bow" becomes a "Uncommon Bow"\n """)
        elif weapon2 == uncommon_bow:
            weapon2 = rare_bow
            print("""Your "Uncommon Bow" becomes a "Rare Bow"\n """)
        elif weapon2 == rare_bow:
            weapon2 = epic_bow
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
    return

def game_start():
    run_preperation()
    round1()


game_start()