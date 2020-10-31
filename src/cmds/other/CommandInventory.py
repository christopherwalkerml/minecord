from src.cmds.Command import Command
from src.utility.User import User
from src.loot.Item import Item
import src.utility.Global as Global

import discord

class CommandInventory(Command):

    def __init__(self, command, info):
        Command.__init__(self, command, [], info)

    async def run(self, message):
        user = User(message.author.id)
        disc_user = Global.client.get_user(user.userId)

        embed = discord.Embed(title=str(disc_user) + "'s Inventory", color=int(user.cosmetic["embed_colour"], 0))

        if len(user.inventory) > 0:
            for cat in user.inventory:
                items = ""
                if len(user.inventory[cat]) > 0:
                    for i in user.inventory[cat]:
                        if user.inventory[cat][i] > 0:
                            emoji = Item.getEmoji(i)
                            items += f"- {emoji} `{user.inventory[cat][i]} {i}`\n"

                if items == "":
                    items = "Empty!"

                embed.add_field(name=cat.capitalize(), value=items)
        else:
            embed.add_field(name="Your inventory is empty!", value="You have no items!")

        embed.set_thumbnail(url=disc_user.avatar_url)

        await message.channel.send(embed=embed)
