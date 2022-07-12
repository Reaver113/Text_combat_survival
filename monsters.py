class monster:
    def __init__(self, name, health, weakness1, weakness2, gold_drop,):
        self.name = name
        self.health = health
        self.weakness1 = weakness1
        self.weakness2 = weakness2
        self.gold_drop = gold_drop

goblin = monster("Goblin", 30, "Slash", "fire", 10)
rock_monster = monster("Rock monster", 40, "Slash", "wind", 15)
cyclops = monster("Cyclops", 50, "Pierce", "earth", 30)
dragon_boss = monster("DRAGON!!!", 160, "Pierce", "water", 80)