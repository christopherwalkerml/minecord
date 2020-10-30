from src.loot.Item import Item
import src.utility.Global as Global

class User:

    def __init__(self, uid, data=None):
        self.userId = uid
        if data is None:
            self.properties = {
                "pickaxe_level": 0,
                "sword_level": 0,
                "enchantment_sharpness": 0,
                "enchantment_looting": 0,
                "experience": 0
            }
            self.cosmetic = {
                "embed_colour": 0x2C2F33
            }
            self.inventory = {}
            self.stats = {
                "chests": {
                    "basic": 0,
                    "common": 0,
                    "uncommon": 0,
                    "rare": 0,
                    "epic": 0
                },
                "ores": {
                    "basic": 0,
                    "common": 0,
                    "uncommon": 0,
                    "rare": 0,
                    "epic": 0
                },
                "bosses": {
                    "basic": 0,
                    "common": 0,
                    "uncommon": 0,
                    "rare": 0,
                    "epic": 0
                }
            }
        else:
            print(data)

    def __repr__(self):
        return f"<User userId: {self.userId}\n" \
               f"inventory: {self.inventory}\n" \
               f"stats: {self.stats}>"

    # items is a list of itemstacks
    def giveItems(self, items):
        for i in items:
            name = i.item.name
            category = Item.getCategory(name)
            count  = i.count

            if name == "experience":
                self.updateProperties("experience", count)
                continue

            if category not in self.inventory:
                self.inventory[category] = {}

            if i.item.name in self.inventory[category]:
                self.inventory[category][name] += count
            else:
                self.inventory[category][name] = count

    def addStat(self, key, stat):
        self.stats[key][stat] += 1

    def updateProperties(self, prop, value):
        self.properties[prop] = value

    def save(self):
        Global.sql.insert("user_properties", ["user_id"] + [p for p in self.properties], [self.userId] + [self.properties[p] for p in self.properties])
        Global.sql.insert("user_cosmetic", ["user_id"] + [p for p in self.cosmetic], [self.userId] + [self.cosmetic[p] for p in self.cosmetic])

        statsstr = ["user_id"]
        stats = [self.userId]
        for s in self.stats:
            for k in self.stats[s]:
                statsstr.append(f"{s}_{k}")
                stats.append(self[s][k])

        Global.sql.insert("user_stats", statsstr, stats)
        pass
