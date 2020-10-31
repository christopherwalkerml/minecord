from src.cmds.Command import Command
from src.crafting.CraftingManager import CraftingManager

class CommandCraft(Command):

    def __init__(self, cmd, optionals, info):
        Command.__init__(self, cmd, optionals, info)

    def run(self, message):
        pass
