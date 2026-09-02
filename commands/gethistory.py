from commands.command import Command
from util.step_history import Step_History


class Get_History(Command):
    name: str = 'gethistory'
    description: str = 'Prints move history'
    counts_as_turn: bool = False

    def execute_command(self, _player_input):
        step_history = Step_History()
        print(step_history.history_as_string())

