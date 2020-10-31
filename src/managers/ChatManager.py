from src.cmds.Command import Command
from src.cmds.config.CommandConfig_Enable import CommandConfig_Enable
from src.cmds.config.CommandConfig_Disable import CommandConfig_Disable
from src.cmds.config.CommandConfig_Get import CommandConfig_Get
from src.cmds.other.CommandInventory import CommandInventory
from src.cmds.other.CommandHelp import CommandHelp
from src.cmds.game.CommandLoot import CommandLoot
from src.utility.User import User

import src.utility.Global as Global

commands = {
    "Game Commands": [
        CommandLoot(["open"], ["<key>"], "Collects a loot chest"),
        CommandLoot(["mine"], ["<key>"], "Mines an ore"),
        CommandLoot(["attack"], ["<key>"], "Attacks an enemy"),
        Command(["recipes"], [], "View a list of all recipes"),
        Command(["recipe"], ["<item>"], "View a single recipe"),
        Command(["craft"], ["<item>"], "Craft an item")
    ],
    "config": [
        CommandConfig_Enable(["config", "enable"], ["#channel"], "Enable bot messages in a channel"),
        CommandConfig_Disable(["config", "disable"], ["#channel"], "Disable bot messages in a channel"),
        CommandConfig_Get(["config", "get"], "Get channels in which bot messages are enabled"),
    ],
    "other": [
        CommandInventory(["inventory"], "View your inventory")
    ]
}
commands["other"].append(CommandHelp(["help"], "shows this text block", commands))

async def messageHandler(message):
    if not message.author.bot:
        content = message.content.lower()
        author = message.author

        if content.startswith(Global.prefix):

            if author.id not in Global.sql.get_users():
                User(author.id, True)

            msgs = content.split()
            msgs[0] = msgs[0].replace(Global.prefix, "")

            for headers in commands:
                header = commands[headers]
                for c in header:
                    match = True
                    for s in range(len(c.command)):
                        if msgs[s] != c.command[s]:
                            match = False
                            break
                        if len(msgs) < len(c.command):
                            break
                    if match:
                        await c.run(message)
                        return

        else:
            if len(Global.sql.get_channels()) > 0:
                await Global.watcher.watch()
