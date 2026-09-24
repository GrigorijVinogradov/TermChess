import board.board_initializer as board_initializer
import board.board_renderer as board_renderer
from commands.command import Command
from commands.help import Help
from commands.command_list import Command_List
from commands.turn import Turn
from util.current_color_keeper import Current_Color_Keeper

def turn():
    current_color = Current_Color_Keeper().get_current_color()
    was_turn_made = False
    while(was_turn_made == False):
        turn_input = input(current_color.name + "s Turn: ")
        command_to_execute: Command = Turn()
        for com in Command_List:
            if turn_input.startswith(com.name):
                command_to_execute = com
        try:
            command_to_execute.execute_command(turn_input)
            was_turn_made = command_to_execute.counts_as_turn
        except ValueError as e: 
            print("Invalid Turn! " + str(e))

board_initializer.initialize_board()
Command_List.append(Help())

while True:
    board_renderer.render_board()
    turn()
    
