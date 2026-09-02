import sys
from commands.command import Command
from util.screen_clearer import clear_screen

class Exit(Command):
    name: str = 'exit'
    description: str = 'Exits the Program'
    counts_as_turn: bool = False

    def execute_command(self, _):
        clear_screen()
        sys.exit()

