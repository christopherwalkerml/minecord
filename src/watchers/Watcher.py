from src.loot.LootManager import LootManager
import src.utility.Global as Global

import discord
from datetime import datetime, timedelta
from random import randrange

class Watcher:

    def __init__(self):
        self.last = datetime.now()
        self.cooldown = 1  # time in seconds for watcher cooldown
        self.current = None

        self.boss_cooldown_set = 10
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

        if val < 30 and self.boss_cooldown <= 0:
            self.boss_cooldown = self.boss_cooldown_set
            self.current = LootManager.generateLoot(LootManager.bosses)
            self.boss = True
            await self.createBoss(self.current)
            return

        self.boss_cooldown -= 1
        self.current = loot
        await self.send(loot)

    @staticmethod
    async def send(loot):
        src = loot.rarity + ".png"
        file = discord.File(loot.src + src, filename=src)
        embed = discord.Embed()
        embed.add_field(name=src.replace(".png", "").capitalize() + " " + loot.type + " has appeared", value="Type `" + Global.prefix + loot.command + " " + loot.rolled_key + "` to get it")
        embed.set_thumbnail(url="attachment://" + src)
        await Global.channels[randrange(len(Global.channels))].send(file=file, embed=embed)

    @staticmethod
    async def createBoss(boss):
        src = boss.rarity + ".png"
        file = discord.File(boss.src + src, filename=src)
        embed = discord.Embed()
        embed.add_field(name=src.replace(".png", "").capitalize() + " " + boss.type + " has appeared", value="Type `" + Global.prefix + boss.command + " " + boss.getKey() + "` to get it")
        embed.set_image(url="attachment://" + src)
        await Global.channels[randrange(len(Global.channels))].send(file=file, embed=embed)
