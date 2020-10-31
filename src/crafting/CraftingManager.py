from .Recipe import Recipe

class CraftingManager:

    furnace = [772108688890527744, "https://static.wikia.nocookie.net/minecraft_gamepedia/images/3/34/Lit_Furnace_JE3_BE2.png/revision/latest"]
    crafting_table = [772108703071600642, "https://static.wikia.nocookie.net/minecraft_gamepedia/images/9/93/Crafting_Table_JE3_BE2.png/revision/latest"]

    recipes = {
        "basic" : [
            Recipe("crafting table", {"oak plank": 4},
                   [["oak plank",   "oak plank"],
                    ["oak plank",   "oak plank"]], requires_table=False),

            Recipe("furnace", {"cobblestone": 8},
                   [["cobblestone", "cobblestone",  "cobblestone"],
                    ["cobblestone", None,           "cobblestone"],
                    ["cobblestone", "cobblestone",  "cobblestone"]])
            ],
        "pickaxes": [
            Recipe("wooden pickaxe", {"oak plank": 3, "stick": 2},
                   [["oak plank",   "oak plank",    "oak plank"],
                    [None,          "stick",        None],
                    [None,          "stick",        None]], item_level=1),

            Recipe("stone pickaxe", {"cobblestone": 3, "stick": 2},
                    [["cobblestone","cobblestone",  "cobblestone"],
                    [None,          "stick",        None],
                    [None,          "stick",        None]], item_level=2),

            Recipe("iron pickaxe", {"iron ingot": 3, "stick": 2},
                   [["iron ingot",  "iron ingot",   "iron ingot"],
                    [None,          "stick",        None],
                    [None,          "stick",        None]], item_level=3),

            Recipe("diamond pickaxe", {"diamond": 3, "stick": 2},
                   [["diamond",     "diamond",      "diamond"],
                    [None,          "stick",        None],
                    [None,          "stick",        None]], item_level=4),

            Recipe("netherite pickaxe", {"netherite ingot": 3, "stick": 2},
                   [["netherite ingot", "netherite ingot",  "netherite ingot"],
                    [None,          "stick",        None],
                    [None,          "stick",        None]], item_level=4)
        ],
        "swords": [
            Recipe("wooden sword", {"oak plank": 2, "stick": 1},
                   [[None, "oak plank", None],
                    [None, "oak plank", None],
                    [None, "stick", None]], item_level=1),

            Recipe("stone sword", {"cobblestone": 2, "stick": 1},
                   [[None, "cobblestone", None],
                    [None, "cobblestone", None],
                    [None, "stick", None]], item_level=2),

            Recipe("iron sword", {"iron ingot": 2, "stick": 1},
                   [[None, "iron ingot", None],
                    [None, "iron ingot", None],
                    [None, "stick", None]], item_level=3),

            Recipe("diamond sword", {"diamond": 2, "stick": 1},
                   [[None, "diamond", None],
                    [None, "diamond", None],
                    [None, "stick", None]], item_level=4),

            Recipe("netherite sword", {"netherite ingot": 2, "stick": 1},
                   [[None, "netherite ingot", None],
                    [None, "netherite ingot", None],
                    [None, "stick", None]], item_level=5),
        ],
        "metals": [
            Recipe("iron ingot", {"iron ore": 1, "coal": 1},
                   [["iron ore", "coal"]], requires_furnace=True),

            Recipe("gold ingot", {"gold ore": 1, "coal": 1},
                   [["gold ore", "coal"]], requires_furnace=True),

            Recipe("netherite scrap", {"ancient debris": 1, "coal": 1},
                   [["ancient debris", "coal"]], requires_furnace=True),

            Recipe("netherite ingot", {"netherite scrap": 4, "gold ingot": 4},
                   [["netherite scrap", "netherite scrap", "netherite scrap"],
                    ["netherite scrap", "gold ingot", "gold ingot"],
                    "gold ingot", "gold ingot", None]),
        ]
    }
