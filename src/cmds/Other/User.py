

class User:

    def __init__(self):
        self.userId = ""
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
