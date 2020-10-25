from random import randrange

class Loot:

    def __init__(self, chance, rarity, loot_table, key_table):
        self.chance = chance
        self.rarity = rarity
        self.loot_table = loot_table
        self.key_table = key_table

        self.rolled_key = self.getItem()
        self.rolled_key = self.getKey()

    def getKey(self):
        return self.key_table[randrange(len(self.key_table))]

    def getItem(self):
        items = []

        for l in self.loot_table:
            if randrange(100) <= l["chance"]:
                items.append(l["item"])

        return items

    def command(self):
        pass
