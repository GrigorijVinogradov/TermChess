from commands.command import Command
from util.step_history import Step_History


class Get_History(Command):
    name: str = 'gethistory'
    counts_as_turn: bool = False

    def execute_command(self, _):
        step_history = Step_History()
        print(step_history.history_as_string())

