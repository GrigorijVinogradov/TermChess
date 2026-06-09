import board.board_initializer as board_initializer
import board.board_renderer as board_renderer
import board.constants.colors as Colors
import re

from board.board import Board
from board.pieces_v2.piece import Piece

def turn(board: Board, current_color: Colors.Color):
    was_turn_made = False
    while(was_turn_made == False):
        turn_input = input("Turn: ")
        try:
            validate_order(turn_input, board, current_color)
            parsed_input = parse_input(turn_input)
            board.move_piece(parsed_input[0], parsed_input[1], parsed_input[2], parsed_input[3])
            was_turn_made = True
        except ValueError as e: 
            print("Invalid Turn! " + str(e))
    return board.get_board_map()

def parse_input(turn_input):
    validate_input(turn_input)
    turn_input = turn_input.replace(" ", "")
    fromL = parse_letter_input(turn_input[0])
    fromD = parse_digit_input(turn_input[1]) 
    toL   = parse_letter_input(turn_input[2])
    toD   = parse_digit_input(turn_input[3]) 
    return [fromD, fromL, toD, toL]

def validate_input(player_input):
    pattern = re.compile(r'[A-H][1-8]\s*[A-H][1-8]\s*', re.IGNORECASE)
    if(bool(pattern.match(player_input)) == False):
        raise ValueError("Input is formatted incorrectly ([A-H][1-8] [A-H][1-8] expected)")

def validate_order(player_input, board: Board, expected_color):
    parsed_input = parse_input(player_input)

    piece = board.get_piece(parsed_input[0], parsed_input[1])
    if not isinstance(piece, Piece):
        raise ValueError("No Piece here!")

    if piece.color != expected_color:
        raise ValueError("Played piece is not the right color")

def parse_letter_input(letter):
    letter = letter.lower()
    digit = ord(letter) - 97
    return digit

def parse_digit_input(digit):
    return 8 - int(digit)

chessboard = Board()
board_initializer.initialize_board(chessboard)

while True:
    board_renderer.render_board(chessboard)
    turn(chessboard, Colors.Color.White)
    board_renderer.render_board(chessboard)
    turn(chessboard, Colors.Color.Black)
