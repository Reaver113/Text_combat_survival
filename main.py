import random
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

def run_preperation():
    global current_enemy
    global enemy_1
    global enemy_2
    global enemy_3
    global enemy_4
    global current_enemy_health_g

    enemy_roll1 = random.randint(1,3)
    if enemy_roll1 == 1:
        enemy1 = goblin
    elif enemy_roll1 == 2:
        enemy1 = rock_monster
    elif enemy_roll1 == 3:
        enemy1 = cyclops

    enemy_roll2 = random.randint(1,3)
    if enemy_roll2 == 1:
        enemy2 = goblin
    elif enemy_roll2 == 2:
        enemy2 = rock_monster
    elif enemy_roll2 == 3:
        enemy2 = cyclops

    enemy_roll3 = random.randint(1,3)
    if enemy_roll3 == 1:
        enemy3 = goblin
    elif enemy_roll3 == 2:
        enemy3 = rock_monster
    elif enemy_roll3 == 3:
        enemy3 = cyclops

    enemy_roll4 = random.randint(1,3)
    if enemy_roll4 == 1:
        enemy4 = goblin
    elif enemy_roll4 == 2:
        enemy4 = rock_monster
    elif enemy_roll4 == 3:
        enemy4 = cyclops


    user_ready = "not ready"
    
    print("This rounds gauntlet will be!\n")
    print(enemy1.name)
    print(f"This enemy has {enemy1.health} Health, and is weak to {enemy1.weakness1} and {enemy1.weakness2} damage\n ")
    print("followed by:\n")
    print(enemy2.name)
    print(f"This enemy has {enemy2.health} Health, and is weak to {enemy2.weakness1} and {enemy2.weakness2} damage\n")
    print("followed by:\n")
    print(enemy3.name)
    print(f"This enemy has {enemy3.health} Health, and is weak to {enemy3.weakness1} and {enemy3.weakness2} damage\n")
    print("followed by:\n")
    print(enemy4.name )
    print(f"This enemy has {enemy4.health} Health, and is weak to {enemy4.weakness1} and {enemy4.weakness2} damage\n")
    print("Goodluck.... you're gonna need it....")
    while user_ready != "ready" or "exit":
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
            break




def round1():
    global round_count
    global has_played
    action = "not ready"
    if current_enemy == dragon_boss:
        print("THE MIGHTY DRAGON ROARS!!!!! This be a tough fight")
    if has_played == False:
        print(f"\nYou stand before {current_enemy.name} and prepare yourself.\n")
        has_played = True
    elif has_played == True:
        print(f"The {current_enemy.name} matches you gaze once more")
    while action != "quick attack" or "quick" or "heavy attack" or "heavy" or "brace" or "potions":
        action = input(""""Quick Attack"    "Heavy Attack"       "Stats"        "Potions"      """).lower()
        if action == "quick attack" or "quick":
            quick_attack()
            if current_enemy_health_g < 1:
                print(f"You have slain the {current_enemy.name}")
                has_played = False
                upgrade()
                round_reset()
            monster_attack()
            if player_health < 1:
                print("You have been defeated")
                return
            else:
                round1()

        elif action == "heavy attack" or "heavy":
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
        elif action == "potions":
            potions()





def quick_attack():
    global current_enemy_health_g
    chosen_weapon = "not chosen"
    while chosen_weapon != weapon1.weapon_name or "sword" or weapon2.weapon_name or "bow":
        chosen_weapon = input(f"\nUse your {weapon1.weapon_name} or {weapon2.weapon_name}: ").lower()
        if chosen_weapon == weapon1.weapon_name or "sword":
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
        if chosen_weapon == weapon2.weapon_name or "bow":
            print(f"You attack with your {weapon2.weapon_name}\n")
            hit_chance = random.randint(1,100)
            if hit_chance > 25 and weapon2.weapon_dmg_type == current_enemy.weakness1:
                print(f"It Hits! ({weapon2.weapon_dmg}) + ({weapon2.weapon_dmg / 4} Weakness bonus")
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
    while chosen_weapon != weapon1.weapon_name or "sowrd" or weapon2.weapon_name or "bow":
        chosen_weapon = input(f"\nUse your {weapon1.weapon_name} or {weapon2.weapon_name}: ").lower()
        if chosen_weapon == weapon1.weapon_name or "sword":
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
        if chosen_weapon == weapon2.weapon_name or "bow":
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
        print(f"The {enemy_1.name} Hits you back for {monster_dmg} ({monster_dmg_pre} + {monster_dmg_pre / 2}) - {helm.dmg_reduction + armor.dmg_reduction} from armor stats)")
        print(f"You have {player_health} remaing\n")
    if current_enemy != dragon_boss:
        monster_dmg_pre = random.randint(10, 20)
        monster_dmg = monster_dmg_pre - helm.dmg_reduction - armor.dmg_reduction
        player_health = player_health - monster_dmg
        print(f"The {enemy_1.name} Hits you back for {monster_dmg} ({monster_dmg_pre} - {helm.dmg_reduction + armor.dmg_reduction} from armor stats)")
        print(f"You have {player_health} remaing\n")



def stats():
    print(f"\nYou current weild a {player.player_weapon1.weapon_name} ({player.player_weapon1.weapon_dmg} Damage) and a {player.player_weapon2.weapon_name} ({player.player_weapon2.weapon_dmg} Damage)")
    print(f"You have donned the {player.armor_head.armor_helm_name} ({player.armor_head.dmg_reduction} Defence) and {player.armor_body.armor_body_name} ({player.armor_body.dmg_reduction} Defence)") 
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



upgrade()