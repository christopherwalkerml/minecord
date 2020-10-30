from src.utility.sendMessage import sendMessage
import src.utility.Global as Global
from src.cmds.Command import Command

class CommandConfig_Enable(Command):

    def __init__(self, command, optionals, info):
        Command.__init__(self, command, optionals, info)

    async def run(self, message):
        channel_m = message.channel_mentions[0]
        if channel_m.id not in Global.sql.get_channels():
            Global.sql.insert("enabled_channels", ["channel_id"], [channel_m.id])
            await sendMessage("Added Channel", "successfully added channel " + channel_m.mention, message.channel)
        else:
            await sendMessage("Added Channel", "channel " + channel_m.mention + " already enabled", message.channel)
