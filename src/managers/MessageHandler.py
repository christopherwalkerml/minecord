from src.cmds.Command import Command
from src.cmds.Config.CommandConfig_Enable import CommandConfig_Enable
from src.cmds.Config.CommandConfig_Disable import CommandConfig_Disable
from src.cmds.Config.CommandConfig_Get import CommandConfig_Get
from src.cmds.Other.CommandInventory import CommandInventory
from src.cmds.Other.CommandHelp import CommandHelp
from src.utility.User import User

import src.utility.Global as Global

commands = {
    "Game Commands": [
        Command(["open"], ["<key>"], "Collects a loot chest"),
        Command(["mine"], ["<key>"], "Mines an ore"),
        Command(["attack"], ["<key>"], "Attacks an enemy")
    ],
    "Config": [
        CommandConfig_Enable(["config", "enable"], ["#channel"], "Enable bot messages in a channel"),
        CommandConfig_Disable(["config", "disable"], ["#channel"], "Disable bot messages in a channel"),
        CommandConfig_Get(["config", "get"], "Get channels in which bot messages are enabled"),
    ],
    "Other": [
        CommandInventory(["inventory"], "View your inventory")
    ]
}
commands["Other"].append(CommandHelp(["help"], "shows this text block", commands))

async def messageHandler(message):
    if not message.author.bot:
        content = message.content.lower()
        author = message.author
        if content.startswith(Global.prefix):

            if author.id not in Global.sql.get_users():
                user = User(author.id)
                user.save()

            msgs = content.split()
            msgs[0] = msgs[0].replace(Global.prefix, "")

            if Global.watcher.currentLoot is not None:
                if msgs[0] == Global.watcher.currentLoot.command:
                    if len(msgs) > 1:
                        if msgs[1] == Global.watcher.currentLoot.rolled_key:
                            await Global.watcher.currentLoot.updateLoot(Global.sql.get_user(author.id))
                            await message.delete()
                        return

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

        else:
            if len(Global.sql.get_channels()) > 0:
                await Global.watcher.watch()
