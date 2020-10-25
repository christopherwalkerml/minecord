import discord

class Command:

    def __init__(self, cmd, info):
        self.command = cmd
        self.info = info

    def __repr__(self):
        return "<" + str(type(self)) + " command: " + self.command + " info: " + self.info + ">"

    async def run(self, message):
        embed = discord.Embed(color=0x32a852)
        embed.add_field(name=self.command, value=self.info)

        await message.channel.send(embed=embed)
