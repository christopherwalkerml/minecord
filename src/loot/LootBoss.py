from .Loot import Loot

class LootBoss(Loot):

    def __init__(self, chance, rarity, loot_table, key_table, health):
        Loot.__init__(self, chance, rarity, loot_table, key_table)
        self.command = "attack"
        self.type = "boss"
        self.src = "../../images/bosses/"
        self.health = health
