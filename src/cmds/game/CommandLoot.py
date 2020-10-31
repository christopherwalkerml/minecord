from src.cmds.Command import Command
import src.utility.Global as Global

class CommandLoot(Command):

    def __init__(self, cmd, optionals, info):
        Command.__init__(self, cmd, optionals, info)

    def run(self, message):
        msgs = message.content.split()
        msgs[0] = msgs[0].replace(Global.prefix, "")

        if Global.watcher.currentLoot is not None:
            if msgs[0] == Global.watcher.currentLoot.command:
                if len(msgs) > 1:
                    if msgs[1] == Global.watcher.currentLoot.rolled_key:
                        await Global.watcher.currentLoot.updateLoot(User(author.id))
                        await message.delete()
