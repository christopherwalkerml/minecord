from src.loot.Item import Item
import src.utility.Global as Global

class User:

    def __init__(self, uid, userdata=None):
        self.userId = uid

        if userdata is None:
            self.properties = {
                "pickaxe_level": 0,
                "sword_level": 0,
                "enchantment_sharpness": 0,
                "enchantment_looting": 0,
                "experience": 0,
                "emeralds": 0
            }
            self.cosmetic = {
                "embed_colour": "0x2C2F33"
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
            self.properties = {
                "pickaxe_level": userdata[0][1],
                "sword_level": userdata[0][2],
                "enchantment_sharpness": userdata[0][3],
                "enchantment_looting": userdata[0][4],
                "experience": userdata[0][5],
                "emeralds": userdata[0][6]
            }
            self.cosmetic = {
                "embed_colour": userdata[1][1]
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

    def __repr__(self):
        return f"<User userId: {self.userId}\n" \
               f"inventory: {self.inventory}\n" \
               f"stats: {self.stats}>"

    # items is a list of itemstacks
    def giveItems(self, items):
        for i in items:
            name = i.item.name.lower()
            count  = i.count

            if name == "experience":
                self.updateProperties("experience", count)
                continue

            if name in self.inventory:
                self.inventory[name] += count
            else:
                self.inventory[name] = count
        self.save()

    def getInventoryByType(self, item_type):
        return [(m if Item.getCategory(m) == item_type else None) for m in self.inventory]

    def addStat(self, key, stat):
        self.stats[key][stat] += 1
        self.save()

    def updateProperties(self, prop, value):
        self.properties[prop] = value
        self.save()

    def save(self):
        print(self.properties)
        Global.sql.insert("user_properties", ["user_id"] + [p for p in self.properties], [self.userId] + [self.properties[p] for p in self.properties])
        Global.sql.insert("user_cosmetic", ["user_id"] + [c for c in self.cosmetic], [self.userId] + [self.cosmetic[c] for c in self.cosmetic])

        statsstr = ["user_id"]
        stats = [self.userId]
        for s in self.stats:
            for k in self.stats[s]:
                statsstr.append(f"{s}_{k}")
                stats.append(self.stats[s][k])

        Global.sql.insert("user_stats", statsstr, stats)

        itemsstr = ["user_id"]
        items = [self.userId]
        for i in Item.items:
            if Item.getCategory(i) != "other":
                itemsstr.append(Item.getCategory(i) + "_" + i.replace(" ", "_"))
                print(i)
                print(self.inventory)
                if i in self.inventory:
                    items.append(self.inventory[i])
                else:
                    items.append(0)

        Global.sql.insert("user_inventory", itemsstr, items)
        pass
