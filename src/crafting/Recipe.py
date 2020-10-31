from src.utility.User import User
import src.utility.Global as Global
from src.loot.Item import Item

from discord import Embed

class Recipe:

    items = {
        "crafting table": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/9/93/Crafting_Table_JE3_BE2.png/revision/latest",
        "furnace": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/4/49/Furnace_JE3_BE2.png/revision/latest",
        "wooden pickaxe": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/0/0b/Wooden_Pickaxe_JE2_BE2.png/revision/latest",
        "stone pickaxe": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/c/c4/Stone_Pickaxe_JE2_BE2.png/revision/latest",
        "iron pickaxe": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/d1/Iron_Pickaxe_JE3_BE2.png/revision/latest",
        "diamond pickaxe": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/e/e7/Diamond_Pickaxe_JE3_BE3.png/revision/latest",
        "netherite pickaxe": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/d4/Netherite_Pickaxe_JE3.png/revision/latest",
        "wooden sword": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/d/d5/Wooden_Sword_JE2_BE2.png/revision/latest",
        "stone sword": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/b/b1/Stone_Sword_JE2_BE2.png/revision/latest",
        "iron sword": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/8/8e/Iron_Sword_JE2_BE2.png/revision/latest",
        "diamond sword": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/4/44/Diamond_Sword_JE3_BE3.png/revision/latest",
        "netherite sword": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/4/48/Netherite_Sword_JE2.png/revision/latest",
        "iron ingot": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/f/fc/Iron_Ingot_JE3_BE2.png/revision/latest",
        "gold ingot": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/8/8a/Gold_Ingot_JE4_BE2.png/revision/latest",
        "netherite scrap": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/3/33/Netherite_Scrap_JE2_BE1.png/revision/latest",
        "netherite ingot": "https://static.wikia.nocookie.net/minecraft_gamepedia/images/5/57/Netherite_Ingot_JE1.png/revision/latest"
    }

    def __init__(self, key, required_items, grid, requires_table=True, requires_furnace=False, item_level=0):
        self.key = key
        self.required_items = required_items
        self.grid = grid
        self.requires_table = requires_table
        self.requires_furnace = requires_furnace
        self.item_level = item_level

    async def craft(self, uid, channel):
        user = User(uid)

        for c in self.required_items:
            if user.getItemCount(c) < self.required_items[c]:
                await self.fail_craft(user, channel)
                return

        if self.requires_table and user.properties["crafting_table"]:
            user.takeItems(self.required_items)
            await self.complete_craft(user, channel)
            return

        if self.requires_furnace and user.properties["furnace"]:
            user.takeItems(self.required_items)
            await self.complete_craft(user, channel)
            return

        await self.fail_craft(user, channel)

    async def complete_craft(self, user, channel):
        text = ""
        if not self.requires_furnace:
            for i, x in enumerate(self.grid):
                for y in x:
                    text += Item.getEmoji(y)

                if i == 1:
                    text += "    >    " + Item.getEmoji(self.key)
                text += "\n"
        else:
            text += Item.getEmoji(self.grid[0][0]) + "\n"
            text += f":fire:    >    {Item.getEmoji(self.key)}\n"
            text += Item.getEmoji(self.grid[0][1]) + "\n"

        embed = Embed()
        embed.colour = int(user.cosmetic["embed_colour"], 0)
        embed.set_thumbnail(url=Recipe.items[self.key])
        embed.add_field(name=str(Global.client.get_user(user.userId)) + " crafted " + self.key, value=text)
        await channel.send(embed)

    async def fail_craft(self, user, channel):
        embed = Embed()
        embed.colour = int(user.cosmetic["embed_colour"], 0)
        embed.set_thumbnail(url=Recipe.items[self.key])
        embed.add_field(name=str(Global.client.get_user(user.userId)) + " failed to craft " + self.key, value="You do not have the required items!")
        await channel.send(embed)
