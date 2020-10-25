from .LootChest import LootChest
from .LootOre import LootOre
from .LootBoss import LootBoss

from random import randrange


class LootManager:

    chests = [
        LootChest(20, "basic",
                  [{"chance": 50, "item": "Stick"},
                   {"chance": 50, "item": "Oak Plank"}],
                  ["basic", "cardboard"]),

        LootChest(30, "common",
                  [{"chance": 50, "item": "Cobblestone"},
                   {"chance": 50, "item": "Oak Log"}],
                  ["common", "barrel"]),

        LootChest(25, "uncommon",
                  [{"chance": 50, "item": "Iron Ingot"},
                   {"chance": 50, "item": "Stone"}],
                  ["uncommon", "chest"]),

        LootChest(15, "rare",
                  [{"chance": 50, "item": "Gold Ingot"},
                   {"chance": 50, "item": "Redstone"}],
                  ["rare", "present", "gift"]),

        LootChest(10, "epic",
                  [{"chance": 50, "item": "Diamond"},
                   {"chance": 50, "item": "Obsidian"}],
                  ["epic", "enderchest", "mystery"]),
    ]

    ores = [
        LootOre(100, "basic",
                [{"chance": 50, "item": "Coal"},
                 {"chance": 50, "item": "Cobblestone"}],
                ["basic", "coal"]),
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
                return l
