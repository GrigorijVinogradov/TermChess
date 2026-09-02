from commands.command import Command
from commands.command_list import Command_List

class Help():
    name: str = 'help'
    description: str = 'Prints all Commandnames and a short description'
    counts_as_turn: bool = False

    def execute_command(self, _):
        for command in Command_List:    
            print('')
            print(command.name + ' - ' + command.description)
        print('')
