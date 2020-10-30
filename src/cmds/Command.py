import discord

class Command:

    def __init__(self, cmd, optionals, info):
        self.command = cmd
        self.info = info
        self.optionals = optionals

    def __repr__(self):
        return "<" + str(type(self)) + " command: " + ' '.join(self.command) + " optionals: " + ' '.join(self.optionals) + " info: " + self.info + ">"

    async def run(self, message):
        embed = discord.Embed(color=0x32a852)
        embed.add_field(name=' '.join(self.command) + " " + ' '.join(self.optionals), value=self.info)

        await message.channel.send(embed=embed)
