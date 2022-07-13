class Monster:
    def __init__(self, name, health, weakness1):
        self.name = name
        self.health = health
        self.weakness1 = weakness1

goblin = Monster("Goblin", 30, "Slash")
rock_Monster = Monster("Rock Monster", 40, "Slash")
cyclops = Monster("Cyclops", 50, "Pierce")
treeant = Monster("Treeant", 40, "Pierce")
orc = Monster("Orc", 50, "Slash")
dragon_boss = Monster("DRAGON!!!", 160, "Pierce")