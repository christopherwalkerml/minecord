from src.cmds.Command import Command
import src.utility.Global as Global
from src.utility.util import getUserFromId
from src.loot.Item import Item

import discord

class CommandInventory(Command):

    def __init__(self, command, info):
        Command.__init__(self, command, [], info)

    async def run(self, message):
        user = Global.users.get(message.author.id)
        disc_user = getUserFromId(user.userId)

        embed = discord.Embed(title=str(disc_user) + "'s Inventory", color=user.cosmetic["colour"])

        if len(user.inventory) > 0:
            for cat in user.inventory:
                items = ""
                if len(user.inventory[cat]) > 0:
                    for i in user.inventory[cat]:
                        emoji = Item.getEmoji(i)
                        items += f"- {emoji} `{user.inventory[cat][i]} {i}`\n"
                else:
                    items = "You have no items of this type!"

                embed.add_field(name=cat.capitalize(), value=items)
        else:
            embed.add_field(name="Your inventory is empty!", value="You have no items!")

        embed.set_thumbnail(url=disc_user.avatar_url)

        await message.channel.send(embed=embed)
