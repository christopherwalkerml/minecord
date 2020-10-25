import discord

async def sendMessage(name, value, channel):
    embed = discord.Embed(color=0x32a852)
    embed.add_field(name=name, value=value)

    await channel.send(embed=embed)