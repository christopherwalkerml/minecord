from src.loot.LootChest import LootChest
from src.loot.LootOre import LootOre
from src.loot.LootBoss import LootBoss
from src.loot.Item import Item

from random import randrange


class LootManager:

    chests = [
        LootChest(40, "basic",
              "https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/55/Beehive_JE1_BE1.png/revision/latest",
              [Item([100, 25], "Stick"),
               Item([50], "Oak Plank"),
               Item([15], "Emerald"),
               Item([1], "Magic Stick")],
              ["basic", "cardboard"]),

        LootChest(25, "common",
              "https://static.wikia.nocookie.net/minecraft_gamepedia/images/8/82/Barrel_JE1_BE1.png/revision/latest",
              [Item([100, 75], "Stick"),
               Item([75], "Oak Plank"),
               Item([25], "Emerald"),
               Item([1], "Mahogany Plank")],
              ["common", "barrel"]),

        LootChest(20, "uncommon",
              "https://static.wikia.nocookie.net/minecraft_gamepedia/images/b/bd/Chest_%28S%29_JE2_BE2.png/revision/latest",
              [Item([100, 25], "Oak Plank"),
               Item([50], "Emerald"),
               Item([5], "Chest"),
               Item([1], "Sipsco High Quality Dirt")], # to updateeeeeeeeeeeeeeeeeeeeee
              ["uncommon", "chest"]),

        LootChest(10, "rare",
              "https://static.wikia.nocookie.net/minecraft_gamepedia/images/9/9d/Xmas_chest.png/revision/latest",
              [Item([100, 25], "Emerald"),
               Item([75], "Oak Plank"),
               Item([15], "Chest"),
               Item([1], "Locked Chest"),
               Item([1], "Snowglobe")],
              ["rare", "present", "gift"]),

        LootChest(5, "epic",
              "https://static.wikia.nocookie.net/minecraft_gamepedia/images/4/41/Ender_Chest_%28S%29_JE2_BE2.png/revision/latest",
              [Item([100, 100, 90, 75], "Emerald"),
               Item([50], "Oak Plank"),
               Item([30], "Chest"),
               Item([15], "Key"),
               Item([5], "Locked Chest"),
               Item([1], "Enchanted Book"),
               Item([1], "Unopenable Chest")],
              ["epic", "enderchest", "mystery"]),
    ]

    ores = [
        LootOre(40, "basic",
            "https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/d6/Coal_Ore_JE2_BE2.png/revision/latest",
            [Item([100], "Cobblestone"),
             Item([100, 25], "Coal"),
             Item([1], "Raw Carbon Fibre")],
            ["basic", "coal"]),

        LootOre(25, "common",
            "https://static.wikia.nocookie.net/minecraft_gamepedia/images/0/0c/Iron_Ore_JE3.png/revision/latest",
            [Item([25, 15], "Coal"),
             Item([100], "Iron Ore"),
             Item([1], "Rusty Magnet")],
            ["common", "iron"]),

        LootOre(20, "uncommon",
            "https://static.wikia.nocookie.net/minecraft_gamepedia/images/b/b9/Gold_Ore_JE3_BE2.png/revision/latest",
            [Item([25, 5], "Coal"),
             Item([100], "Gold Ore"),
             Item([1], "Pile of Doubloons")],
            ["uncommon", "gold"]),

        LootOre(10, "rare",
            "https://static.wikia.nocookie.net/minecraft_gamepedia/images/b/b5/Diamond_Ore_JE3_BE3.png/revision/latest",
            [Item([15, 1], "Coal"),
             Item([100], "Diamond"),
             Item([1], "Diamond Ring")],
            ["rare", "diamond", "shiny"]),

        LootOre(5, "epic",
            "https://static.wikia.nocookie.net/minecraft_gamepedia/images/4/4c/Ancient_Debris_JE1_BE1.png/revision/latest",
            [Item([15], "Diamond"),
             Item([15], "Coal"),
             Item([15], "Iron Ore"),
             Item([15], "Gold Ore"),
             Item([100], "Netherite Ore"),
             Item([1], "Quartz Chunk")],
            ["epic", "netherite", "fireproof"]),
    ]

    bosses = [
        LootBoss(40, "basic",
             "https://static.wikia.nocookie.net/minecraft_gamepedia/images/e/e0/Salmon.png/revision/latest",
             [Item([100, 50, 15], "Emerald"),
              Item([100, 75, 50, 25], "Experience"),
              Item([1], "Locked Chest"),
              Item([1], "Sushi")],
             ["basic", "salmon"], 5),

        LootBoss(25, "common",
             "https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/56/Bee.png/revision/latest",
             [Item([100, 50, 15], "Emerald"),
              Item([100, 75, 50, 25], "Experience"),
              Item([3], "Locked Chest"),
              Item([1], "Hivemind")],
             ["common", "bee"], 10),

        LootBoss(20, "uncommon",
             "https://static.wikia.nocookie.net/minecraft_gamepedia/images/0/0d/Iron_Golem.png/revision/latest",
             [Item([100, 50, 15], "Emerald"),
              Item([100, 75, 50, 25], "Experience"),
              Item([5], "Locked Chest"),
              Item([1], "Key"),
              Item([1], "Laputa Crystal")],
             ["uncommon", "irongolem"], 20),

        LootBoss(10, "rare",
             "https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/aa/Wither.png/revision/latest",
             [Item([100, 50, 15], "Emerald"),
              Item([100, 75, 50, 25], "Experience"),
              Item([7], "Locked Chest"),
              Item([3], "Key"),
              Item([1], "Enchanted Book"),
              Item([1], "Nether Star")],
             ["rare", "wither"], 50),

        LootBoss(5, "epic",
             "https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/5a/Ender_Dragon.png/revision/latest",
             [Item([100, 50, 15], "Emerald"),
              Item([100, 75, 50, 25], "Experience"),
              Item([10], "Locked Chest"),
              Item([5], "Key"),
              Item([5], "Enchanted Book"),
              Item([1], "Dragon Egg")],
             ["epic", "dragon"], 100),
    ]

    @staticmethod
    def generateLoot(loot_table):
        val = randrange(100)

        table = []

        for l in loot_table:
            for chance in range(l.chance):
                table.append(l.rarity)

        chosen = table[val]

        for l in loot_table:
            if l.rarity == chosen:
                l.generate()
                return l
