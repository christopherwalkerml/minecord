from .LootChest import LootChest
from .LootOre import LootOre
from .LootBoss import LootBoss

from random import randrange


class LootManager:

    chests = [
        LootChest(20, "basic",
              "https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/55/Beehive_JE1_BE1.png/revision/latest?cb=20200224220617&format=original",
              [{"chance": [100, 25], "item": "Stick"},
               {"chance": [50], "item": "Oak Plank"},
               {"chance": [25], "item": "Apple"},
               {"chance": [15], "item": "Emerald"}],
              ["basic", "cardboard"]),

        LootChest(30, "common",
              "https://static.wikia.nocookie.net/minecraft_gamepedia/images/8/82/Barrel_JE1_BE1.png/revision/latest?cb=20200224220423&format=original",
              [{"chance": [100, 75], "item": "Stick"},
               {"chance": [75], "item": "Oak Plank"},
               {"chance": [50, 15], "item": "Apple"},
               {"chance": [25], "item": "Emerald"},
               {"chance": [1], "item": "Chest"}],
              ["common", "barrel"]),

        LootChest(25, "uncommon",
              "https://static.wikia.nocookie.net/minecraft_gamepedia/images/b/bd/Chest_%28S%29_JE2_BE2.png/revision/latest?cb=20191230024542&format=original",
              [{"chance": [100, 25], "item": "Oak Plank"},
               {"chance": [50], "item": "Emerald"},
               {"chance": [45, 15], "item": "Pumpkin Pie"},
               {"chance": [5], "item": "Chest"},
               {"chance": [1], "item": "Locked Chest"}],
              ["uncommon", "chest"]),

        LootChest(15, "rare",
              "https://static.wikia.nocookie.net/minecraft_gamepedia/images/9/9d/Xmas_chest.png/revision/latest?cb=20191220024431&format=original",
              [{"chance": [100, 25], "item": "Emerald"},
               {"chance": [75, 45], "item": "Pumpkin Pie"},
               {"chance": [15], "item": "Chest"},
               {"chance": [5], "item": "Locked Chest"},
               {"chance": [1], "item": "Book of Glyphs"}],
              ["rare", "present", "gift"]),

        LootChest(10, "epic",
              "https://static.wikia.nocookie.net/minecraft_gamepedia/images/4/41/Ender_Chest_%28S%29_JE2_BE2.png/revision/latest?cb=20200315175314&format=original",
              [{"chance": [100, 100, 90, 75], "item": "Emerald"},
               {"chance": [70, 50, 15], "item": "Pumpkin Pie"},
               {"chance": [65], "item": "Chest"},
               {"chance": [35], "item": "Key"},
               {"chance": [10], "item": "Locked Chest"},
               {"chance": [5], "item": "Book of Glyphs"},
               {"chance": [1], "item": "Mosaic Painting"}],
              ["epic", "enderchest", "mystery"]),
    ]

    ores = [
        LootOre(20, "basic",
            "https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/d6/Coal_Ore_JE2_BE2.png/revision/latest?cb=20200307223855&format=original",
            [{"chance": [100], "item": "Cobblestone"},
             {"chance": [100, 25], "item": "Coal"}],
            ["basic", "coal"]),

        LootOre(30, "common",
            "https://static.wikia.nocookie.net/minecraft_gamepedia/images/0/0c/Iron_Ore_JE3.png/revision/latest?cb=20200315185600&format=original",
            [{"chance": [50, 15], "item": "Coal"},
             {"chance": [100], "item": "Iron Ore"},
             {"chance": [15], "item": "Emerald"}],
            ["common", "iron"]),

        LootOre(25, "uncommon",
            "https://static.wikia.nocookie.net/minecraft_gamepedia/images/b/b9/Gold_Ore_JE3_BE2.png/revision/latest?cb=20200224211658&format=original",
            [{"chance": [25, 5], "item": "Coal"},
             {"chance": [100], "item": "Gold Ore"},
             {"chance": [40], "item": "Emerald"}],
            ["uncommon", "gold"]),

        LootOre(15, "rare",
            "https://static.wikia.nocookie.net/minecraft_gamepedia/images/b/b5/Diamond_Ore_JE3_BE3.png/revision/latest?cb=20200309195154&format=original",
            [{"chance": [15, 1], "item": "Coal"},
             {"chance": [100], "item": "Diamond"},
             {"chance": [50, 35], "item": "Emerald"}],
            ["rare", "diamond", "shiny"]),

        LootOre(10, "epic",
            "https://static.wikia.nocookie.net/minecraft_gamepedia/images/4/4c/Ancient_Debris_JE1_BE1.png/revision/latest?cb=20200216200020&format=original",
            [{"chance": [100, 100, 75, 45], "item": "Emerald"},
             {"chance": [15], "item": "Diamond"},
             {"chance": [15], "item": "Coal"},
             {"chance": [15], "item": "Iron Ore"},
             {"chance": [15], "item": "Gold Ore"},
             {"chance": [100], "item": "Netherite Ore"},
             {"chance": [1], "item": "Mosaic Geode"}],
            ["epic", "netherite", "fireproof"]),
    ]

    bosses = [
        LootBoss(20, "basic",
             "https://static.wikia.nocookie.net/minecraft_gamepedia/images/e/e0/Salmon.png/revision/latest?cb=20180312083423&format=original",
             [{"chance": [100, 50], "item": "Emerald"},
              {"chance": [100, 75, 50, 25], "item": "Experience"},
              {"chance": [1], "item": "Salmon"}],
             ["basic", "salmon"], 3),

        LootBoss(30, "common",
             "https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/56/Bee.png/revision/latest?cb=20200317180506&format=original",
             [{"chance": [100, 100, 50, 50], "item": "Emerald"},
              {"chance": [100, 100, 75, 75, 50, 50, 25, 25], "item": "Experience"},
              {"chance": [1], "item": "Honeycomb"}],
             ["common", "bee"], 5),

        LootBoss(25, "uncommon",
             "https://static.wikia.nocookie.net/minecraft_gamepedia/images/0/0d/Iron_Golem.png/revision/latest?cb=20190605101959&format=original",
             [{"chance": [100, 100, 50, 50], "item": "Emerald"},
              {"chance": [100, 100, 75, 75, 50, 50, 25, 25], "item": "Experience"},
              {"chance": [1], "item": "Rose"}],
             ["uncommon", "irongolem"], 9),

        LootBoss(15, "rare",
             "https://static.wikia.nocookie.net/minecraft_gamepedia/images/a/aa/Wither.png/revision/latest?cb=20191229161710&format=original",
             [{"chance": [100, 100, 100, 50, 50, 50], "item": "Emerald"},
              {"chance": [100, 100, 100, 75, 75, 75, 50, 50, 50, 25, 25, 25], "item": "Experience"},
              {"chance": [1], "item": "Nether Star"}],
             ["rare", "wither"], 15),

        LootBoss(10, "epic",
             "https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/5a/Ender_Dragon.png/revision/latest?cb=20180225041902&format=original",
             [{"chance": [100, 100, 100, 100, 50, 50, 50, 50], "item": "Emerald"},
              {"chance": [100, 100, 100, 100, 75, 75, 75, 75, 50, 50, 50, 50, 25, 25, 25, 25], "item": "Experience"},
              {"chance": [1], "item": "Dragon Egg"}],
             ["epic", "dragon"], 25),
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
