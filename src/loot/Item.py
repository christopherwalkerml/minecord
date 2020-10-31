from .ItemStack import ItemStack

from random import randrange

class Item:

    items = {
        "stick": [770878560339492874, "material"],
        "oak plank": [770878553143246878, "material"],
        "cobblestone": [770884221610623046, "material"],
        "coal": [770877818288078868, "material"],
        "iron ore": [770878497605812245, "material"],
        "iron ingot": [771577929674915860, "material"],
        "gold ore": [770878490195001366, "material"],
        "gold ingot": [771577941418049586, "material"],
        "diamond": [770877825578303509, "material"],
        "ancient debris": [770878532796153876, "material"],
        "netherite scraps": [771577968702128158, "material"],
        "netherite ingot": [771577951429853194, "material"],
        "chest": [770877788244410408, "special"],
        "key": [770878567541375018, "special"],
        "locked chest": [770878505067741184, "special"],
        "enchanted book": [770878429276143656, "special"],
        "magic stick": [None, "collection"],
        "mahogany plank": [None, "collection"],
        "sipsco high quality dirt": [None, "collection"],
        "snowglobe": [None, "collection"],
        "unopenable chest": [None, "collection"],
        "raw carbon fibre": [None, "collection"],
        "rusty magnet": [None, "collection"],
        "pile of doubloons": [None, "collection"],
        "diamond ring": [None, "collection"],
        "quartz chunk": [None, "collection"],
        "sushi": [None, "collection"],
        "hivemind": [None, "collection"],
        "laputa crystal": [None, "collection"],
        "nether star": [None, "collection"],
        "dragon egg": [None, "collection"],
        "emerald": [770877832603369473, "other"],
        "experience": [770878480820338698, "other"],
    }

    def __init__(self, chance, name):
        self.chance = chance
        self.name = name

    def roll(self):
        count = 0
        for c in self.chance:
            if randrange(100) < c:
                count += 1

        return ItemStack(self, count) if count > 0 else None

    @staticmethod
    def getEmoji(name):
        if name.lower() in Item.items and Item.items[name.lower()][0] is not None:
            ename = name.lower().replace(" ", "_")
            eid = Item.items[name.lower()][0]
            return f"<:{ename}:{eid}>"
        return ""

    @staticmethod
    def getCategory(name):
        if name.lower() in Item.items:
            return Item.items[name.lower()][1]
        else:
            return ""
