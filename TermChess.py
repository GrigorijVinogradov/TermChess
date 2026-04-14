import board.board_initializer as board_initializer
import board.board_renderer as board_renderer
import re

from board.board import Board

def turn(board: Board):
    turn_input = input("Turn: ")
    if(validate_input(turn_input)):
        turn_input = turn_input.replace(" ", "")
        fromL = parse_letter_input(turn_input[0])
        fromD = parse_digit_input(turn_input[1]) 
        toL   = parse_letter_input(turn_input[2])
        toD   = parse_digit_input(turn_input[3]) 
        board.move_piece(fromD, fromL, toD, toL)
    return board.get_board_map()

def validate_input(player_input):
    pattern = re.compile(r'[A-H][1-8]\s*[A-H][1-8]\s*', re.IGNORECASE)
    return bool(pattern.match(player_input))

def parse_letter_input(letter):
    letter = letter.lower()
    digit = ord(letter) - 97
    return digit

def parse_digit_input(digit):
    return 8 - int(digit)

# chessboard = board.get_default_board()

chessboard = Board()
board_initializer.initialize_board(chessboard)

while True:
    board_renderer.render_board(chessboard)
    turn(chessboard)
