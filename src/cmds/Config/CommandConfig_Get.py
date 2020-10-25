from src.utility.Global import *
from src.cmds.Command import Command
from src.utility.sendMessage import sendMessage

class CommandConfig_Get(Command):

    def __init__(self, command, info):
        Command.__init__(self, command, info)

    async def run(self, message):
        cs = ""
        for c in channels:
            cs += "#" + c.name + "\n"
        await sendMessage("Enabled Channels", cs, message.channel)
