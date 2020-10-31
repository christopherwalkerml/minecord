from src.loot.Item import Item
import src.utility.Global as Global

class User:

    def __init__(self, uid, new=False):
        self.userId = uid

        print(new)

        self.properties = {}
        self.cosmetic = {}
        self.inventory = {}
        self.stats = {}

        properties = [("pickaxe_level", 0), ("sword_level", 0), ("enchantment_sharpness", 0), ("enchantment_looting", 0), ("experience", 0), ("emeralds" ,0)]
        cosmetic = [("embed_colour", "0x2C2F33")]
        stats = {
            "chests": [("basic", 0), ("common", 0), ("uncommon", 0), ("rare", 0), ("epic", 0)],
            "ores": [("basic", 0), ("common", 0), ("uncommon", 0), ("rare", 0), ("epic", 0)],
            "bosses": [("basic", 0), ("common", 0), ("uncommon", 0), ("rare", 0), ("epic", 0)]
        }

        if new:
            for p in properties:
                self.properties[p[0]] = p[1]

            for c in cosmetic:
                self.cosmetic[c[0]] = c[1]

            for s in stats:
                self.stats[s] = {}
                for cat in stats[s]:
                    self.stats[s][cat[0]] = cat[1]

            for i in Item.items:
                cat = Item.getCategory(i)
                if cat != "other":
                    if cat not in self.inventory:
                        self.inventory[cat] = {}

                    self.inventory[cat][i] = 0

            self.save()

        else:
            userdata = Global.sql.get_user_data(self.userId)

            print(userdata)

            print('x')

            for p in userdata["properties"]:
                if p == "user_id":
                    continue
                self.properties[p] = userdata["properties"][p]

            for c in userdata["cosmetic"]:
                if c == "user_id":
                    continue
                self.cosmetic[c] = userdata["cosmetic"][c]

            for s in userdata["stats"]:
                if s == "user_id":
                    continue
                cat = s.replace('_', ' ').split()[0]
                rarity = s.replace('_', ' ').split()[1]

                if cat not in self.stats:
                    self.stats[cat] = {}

                self.stats[cat][rarity] = userdata["stats"][s]

            for i in userdata["inventory"]:
                if i == "user_id":
                    continue
                cat = i.replace('_', ' ').split()[0]
                item = i.replace(f"{cat}_", "").replace('_', " ")

                if cat not in self.inventory:
                    self.inventory[cat] = {}

                self.inventory[cat][item] = userdata["inventory"][i]

            print(self.inventory)


    def __repr__(self):
        return f"<User userId: {self.userId}\n" \
               f"inventory: {self.inventory}\n" \
               f"stats: {self.stats}>"

    # items is a list of itemstacks
    def giveItems(self, items):
        for i in items:
            name = i.item.name.lower()
            cat = Item.getCategory(name)
            count  = i.count

            if name == "experience":
                self.addToProperties("experience", count)
                continue

            if name == "emerald":
                self.addToProperties("emeralds", count)
                continue

            self.inventory[cat][name] += count

        self.save_inventory()

    def getInventoryByType(self, item_type):
        return [(m if Item.getCategory(m) == item_type else None) for m in self.inventory]

    def addStat(self, key, stat):
        self.stats[key][stat] += 1
        self.save_stats()

    def addToProperties(self, prop, value):
        self.properties[prop] = self.properties[prop] + value
        self.save_properties()

    def save_properties(self):
        Global.sql.insert("user_properties", ["user_id"] + [p for p in self.properties], [self.userId] + [self.properties[p] for p in self.properties])

    def save_cosmetic(self):
        Global.sql.insert("user_cosmetic", ["user_id"] + [c for c in self.cosmetic], [self.userId] + [self.cosmetic[c] for c in self.cosmetic])

    def save_stats(self):
        statsstr = ["user_id"]
        stats = [self.userId]
        for s in self.stats:
            for k in self.stats[s]:
                statsstr.append(f"{s}_{k}")
                stats.append(self.stats[s][k])

        Global.sql.insert("user_stats", statsstr, stats)

    def save_inventory(self):
        itemsstr = ["user_id"]
        items = [self.userId]
        for i in Item.items:
            cat = Item.getCategory(i)
            if cat != "other":
                itemsstr.append(cat + "_" + i.replace(" ", "_"))

                items.append(self.inventory[cat][i])

        Global.sql.insert("user_inventory", itemsstr, items)

    def save(self):
        self.save_properties()
        self.save_cosmetic()
        self.save_stats()
        self.save_inventory()
