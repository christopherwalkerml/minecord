from .Loot import Loot

class LootChest(Loot):

    def __init__(self, chance, rarity, loot_table, key_table):
        Loot.__init__(self, chance, rarity, loot_table, key_table)
        self.command = "open"
        self.type = "loot box"
        self.src = "../../images/chests/"
