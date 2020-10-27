from src.loot.LootManager import LootManager

from datetime import datetime, timedelta
from random import randrange

class Watcher:

    def __init__(self):
        self.last = datetime.now()
        self.cooldown = 1  # time in seconds for watcher cooldown
        self.currentLoot = None

        self.boss_cooldown_set = 0
        self.boss_cooldown = self.boss_cooldown_set
        self.boss = False

    async def watch(self):
        if self.boss:
            return

        if datetime.now() - self.last > timedelta(seconds=self.cooldown):
            self.last = datetime.now()
            await self.activate()

    async def activate(self):
        val = randrange(100)

        if val > 60:
            loot = LootManager.generateLoot(LootManager.chests)
        else:
            loot = LootManager.generateLoot(LootManager.ores)

        if val < 100 and self.boss_cooldown <= 0:
            self.boss_cooldown = self.boss_cooldown_set
            self.currentLoot = LootManager.generateLoot(LootManager.bosses)
            self.boss = True
            await self.currentLoot.sendLoot()
            return

        self.boss_cooldown -= 1
        self.currentLoot = loot
        await self.currentLoot.sendLoot()
