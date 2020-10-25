from src.utility.sendMessage import sendMessage
from src.utility.Global import *
from src.cmds.Command import Command

class CommandConfig_Enable(Command):

    def __init__(self, command, info):
        Command.__init__(self, command, info)

    async def run(self, message):
        channels.append(message.channel_mentions[0])
        await sendMessage("Added Channel", "successfully added channel #" + message.channel_mentions[0].name, message.channel)
