class monster:
    def __init__(self, name, health, weakness1):
        self.name = name
        self.health = health
        self.weakness1 = weakness1

goblin = monster("Goblin", 30, "Slash")
rock_monster = monster("Rock monster", 40, "Slash")
cyclops = monster("Cyclops", 50, "Pierce")
treeant = monster("Treeant", 40, "Pierce")
orc = monster("Orc", 50, "Slash")
dragon_boss = monster("DRAGON!!!", 160, "Pierce")