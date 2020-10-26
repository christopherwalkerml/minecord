from .LootChest import LootChest
from .LootOre import LootOre
from .LootBoss import LootBoss

from random import randrange


class LootManager:

    chests = [
        LootChest(20, "basic",
              [{"chance": 100, "item": "Stick"},
               {"chance": 50, "item": "Oak Plank"},
               {"chance": 25, "item": "Stick"},
               {"chance": 15, "item": "Emerald"},
               {"chance": 5, "item": "Apple"}],
              ["basic", "cardboard"]),

        LootChest(30, "common",
              [{"chance": 100, "item": "Stick"},
               {"chance": 75, "item": "Stick"},
               {"chance": 50, "item": "Oak Plank"},
               {"chance": 25, "item": "Emerald"},
               {"chance": 20, "item": "Apple"},
               {"chance": 5, "item": "Chest"},
               {"chance": 1, "item": "Locked Chest"}],
              ["common", "barrel"]),

        LootChest(25, "uncommon",
              [{"chance": 100, "item": "Stick"},
               {"chance": 50, "item": "Emerald"},
               {"chance": 25, "item": "Pumpkin Pie"},
               {"chance": 15, "item": "Chest"},
               {"chance": 5, "item": "Locked Chest"},
               {"chance": 1, "item": "Book of Glyphs"}],
              ["uncommon", "chest"]),

        LootChest(15, "rare",
              [{"chance": 100, "item": "Emerald"},
               {"chance": 75, "item": "Pumpkin Pie"},
               {"chance": 50, "item": "Chest"},
               {"chance": 25, "item": "Emerald"},
               {"chance": 15, "item": "Locked Chest"},
               {"chance": 10, "item": "Book of Glyphs"},
               {"chance": 5, "item": "Key"}],
              ["rare", "present", "gift"]),

        LootChest(10, "epic",
              [{"chance": 100, "item": "Emerald"},
               {"chance": 100, "item": "Emerald"},
               {"chance": 90, "item": "Emerald"},
               {"chance": 80, "item": "Chest"},
               {"chance": 75, "item": "Emerald"},
               {"chance": 70, "item": "Pumpkin Pie"},
               {"chance": 65, "item": "Chest"},
               {"chance": 60, "item": "Key"},
               {"chance": 40, "item": "Locked Chest"},
               {"chance": 25, "item": "Book of Glyphs"},
               {"chance": 10, "item": "Pumpkin Pie"},
               {"chance": 5, "item": "Mosaic Painting"}],
              ["epic", "enderchest", "mystery"]),
    ]

    ores = [
        LootOre(20, "basic",
            [{"chance": 100, "item": "Cobblestone"},
             {"chance": 75, "item": "Coal"},
             {"chance": 50, "item": "Cobblestone"},
             {"chance": 25, "item": "Coal"}],
            ["basic", "coal"]),

        LootOre(30, "common",
            [{"chance": 100, "item": "Cobblestone"},
             {"chance": 80, "item": "Coal"},
             {"chance": 75, "item": "Iron Ore"},
             {"chance": 50, "item": "Coal"},
             {"chance": 25, "item": "Iron Ore"},
             {"chance": 15, "item": "Emerald"},
             {"chance": 1, "item": "Key"}],
            ["common", "iron"]),

        LootOre(25, "uncommon",
            [{"chance": 100, "item": "Cobblestone"},
             {"chance": 100, "item": "Coal"},
             {"chance": 80, "item": "Iron Ore"},
             {"chance": 75, "item": "Gold Ore"},
             {"chance": 70, "item": "Coal"},
             {"chance": 50, "item": "Iron Ore"},
             {"chance": 40, "item": "Emerald"},
             {"chance": 25, "item": "Gold Ore"},
             {"chance": 15, "item": "Coal"},
             {"chance": 5, "item": "Key"}],
            ["uncommon", "gold"]),

        LootOre(15, "rare",
            [{"chance": 100, "item": "Coal"},
             {"chance": 100, "item": "Iron Ore"},
             {"chance": 80, "item": "Coal"},
             {"chance": 75, "item": "Gold Ore"},
             {"chance": 75, "item": "Diamond"},
             {"chance": 70, "item": "Emerald"},
             {"chance": 60, "item": "Iron Ore"},
             {"chance": 50, "item": "Coal"},
             {"chance": 40, "item": "Emerald"},
             {"chance": 35, "item": "Gold Ore"},
             {"chance": 25, "item": "Diamond"},
             {"chance": 10, "item": "Key"},
             {"chance": 5, "item": "Netherite Ore"}],
            ["rare", "diamond", "shiny"]),

        LootOre(10, "epic",
            [{"chance": 100, "item": "Diamond"},
             {"chance": 100, "item": "Emerald"},
             {"chance": 100, "item": "Emerald"},
             {"chance": 90, "item": "Coal"},
             {"chance": 80, "item": "Iron Ore"},
             {"chance": 75, "item": "Gold Ore"},
             {"chance": 75, "item": "Netherite Ore"},
             {"chance": 75, "item": "Emerald"},
             {"chance": 60, "item": "Diamond"},
             {"chance": 60, "item": "Key"},
             {"chance": 60, "item": "Iron Ore"},
             {"chance": 50, "item": "Coal"},
             {"chance": 45, "item": "Emerald"},
             {"chance": 35, "item": "Diamond"},
             {"chance": 25, "item": "Netherite Ore"},
             {"chance": 15, "item": "Rainbow Geode"},
             {"chance": 5, "item": "Netherite Ore"}],
            ["epic", "netherite", "fireproof"]),
    ]

    bosses = [
        LootBoss(20, "basic",
             [{"chance": 50, "item": "Leather"},
              {"chance": 50, "item": "Beef"}],
             ["basic", "salmon"], 5),

        LootBoss(30, "common",
             [{"chance": 50, "item": "Leather"},
              {"chance": 50, "item": "Beef"}],
             ["common", "bee"], 5),

        LootBoss(25, "uncommon",
             [{"chance": 50, "item": "Leather"},
              {"chance": 50, "item": "Beef"}],
             ["uncommon", "irongolem"], 5),

        LootBoss(15, "rare",
             [{"chance": 50, "item": "Leather"},
              {"chance": 50, "item": "Beef"}],
             ["rare", "wither"], 5),

        LootBoss(10, "epic",
             [{"chance": 50, "item": "Leather"},
              {"chance": 50, "item": "Beef"}],
             ["epic", "dragon"], 5),
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
