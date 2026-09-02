from commands.command import Command
from commands.command_list import Command_List

class Help():
    name: str = 'help'
    counts_as_turn: bool = False

    def execute_command(self, _):
        for command in Command_List:    
            print(command.name)
