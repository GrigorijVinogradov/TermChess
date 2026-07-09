import board.board_initializer as board_initializer
import board.board_renderer as board_renderer
from commands.command import Command
from commands.turn import Turn
import pieces.enums.colors as Colors

def turn(current_color: Colors.Color):
    was_turn_made = False
    while(was_turn_made == False):
        turn_input = input(current_color.name + "s Turn: ")
        command_to_execute: Command = Turn()
        for com in command_list:
            if com.name == turn_input:
                command_to_execute = com
        try:
            command_to_execute.execute_command(turn_input, current_color)
            was_turn_made = command_to_execute.counts_as_turn
        except ValueError as e: 
            print("Invalid Turn! " + str(e))

board_initializer.initialize_board()

command_list = [ Command() ]

while True:
    board_renderer.render_board()
    turn(Colors.Color.White)
    board_renderer.render_board()
    turn(Colors.Color.Black)
