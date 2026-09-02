import time

from commands.command import Command
from textwrap import wrap

from commands.turn import Turn

class Play_Sequence(Command):
    name: str = 'playsequence'
    description: str = 'Plays a sequence of Steps, which are notated like regular moves after the command'
    counts_as_turn: bool = True

    def execute_command(self, player_input: str):
        sequence_string = player_input.removeprefix(self.name)
        sequence_string = sequence_string.replace(" ", "")
        split_sequence = wrap(sequence_string, 4)

        turn_command = Turn()
        for step in split_sequence:
            try:
                turn_command.execute_command(step)
            except ValueError as e:
                print("failed at " + step + " due to following: " + str(e))
                input("Enter anything to continue ")

