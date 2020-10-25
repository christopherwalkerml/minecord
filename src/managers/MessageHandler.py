from src.cmds.Game.CommandOpen import CommandOpen
from src.cmds.Game.CommandAttack import CommandAttack
from src.cmds.Config.CommandConfig_Enable import CommandConfig_Enable
from src.cmds.Config.CommandConfig_Disable import CommandConfig_Disable
from src.cmds.Config.CommandConfig_Get import CommandConfig_Get
from src.cmds.Other.CommandHelp import CommandHelp

import src.utility.Global as Global

from src.cmds.WinkCommand import *

commands = {
    "Game Commands": [
        CommandOpen("open <key>", "Collects a loot chest"),
        CommandAttack("attack <key>", "Attacks an enemy")
    ],
    "Config": [
        CommandConfig_Enable("config-enable", "Enable bot messages in a channel"),
        CommandConfig_Disable("config-disable", "Disable bot messages in a channel"),
        CommandConfig_Get("config-get", "Get channels in which bot messages are enabled"),
    ],
    "Other": [
    ]
}
commands["Other"].append(CommandHelp("help", "shows this text block", commands))

async def messageHandler(message):
    if len(Global.channels) > 0:
        await Global.watcher.watch()

    if message.content.startswith(Global.prefix):
        msgs = message.content.split()
        msgs[0] = msgs[0].replace(Global.prefix, "")

        if msgs[0] == "wink":  # FOR TESTING
            await getWinkGift(message)
            await getWinkCommandBangScore(message)
            await getWinkCommandMyBang(message)

        for headers in commands:
            header = commands[headers]
            for c in header:
                match = True
                for s in range(len(c.command.replace('-', ' ').split())):
                    if msgs[s] != c.command.replace('-', ' ').split()[s]:
                        match = False
                        break
                if match:
                    await c.run(message)