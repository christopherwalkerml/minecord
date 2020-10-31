from src.utility.Global import *
from src.utility.sendMessage import sendMessage
from src.cmds.Command import Command

class CommandConfig_Disable(Command):

    def __init__(self, command, optionals, info):
        Command.__init__(self, command, optionals, info)

    async def run(self, message):
        if message.channel_mentions[0] in channels:
            channels.remove(message.channel_mentions[0])
            await sendMessage("Removed Channel", "successfully removed channel " + message.channel_mentions[0].mention, message.channel)
        else:
            await sendMessage("Removed Channel", "channel " + message.channel_mentions[0].mention + " not enabled", message.channel)
