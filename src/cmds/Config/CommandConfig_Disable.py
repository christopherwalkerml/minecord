from src.utility.Global import *
from src.utility.sendMessage import sendMessage
from src.cmds.Command import Command

class CommandConfig_Disable(Command):

    def __init__(self, command, info):
        Command.__init__(self, command, info)

    async def run(self, message):
        channels.remove(message.channel_mentions[0])
        await sendMessage("Removed Channel", "successfully removed channel #" + message.channel_mentions[0].name, message.channel)
