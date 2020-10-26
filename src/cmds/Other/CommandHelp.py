import discord

from src.utility.Global import *

from src.cmds.Command import Command

class CommandHelp(Command):

    def __init__(self, command, info, commandlist):
        Command.__init__(self, command, info)
        self.commandlist = commandlist

    async def run(self, message):
        embed = discord.Embed(title="Minecord Game Bot", color=0x32a852)

        for header in self.commandlist:
            commands = self.commandlist[header]
            val = ""
            for cmdobj in commands:
                val += "`" + prefix + cmdobj.command + "` - " + cmdobj.info + "\n"
            embed.add_field(name=header, value=val, inline=False)

        await message.channel.sendLoot(embed=embed)
