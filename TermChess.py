import board.board_initializer as board_initializer
import board.board_renderer as board_renderer
import board.pieces as pieces
import re

from board.board import Board

def turn(board: Board, current_color: str):
    was_turn_made = False
    while(was_turn_made == False):
        turn_input = input("Turn: ")
        is_valid_turn = validate_input(turn_input) and validate_order(turn_input, board, current_color)
        if(is_valid_turn):
            parsed_input = parse_input(turn_input)
            board.move_piece(parsed_input[0], parsed_input[1], parsed_input[2], parsed_input[3])
            was_turn_made = True
        else: 
            print("Invalid Turn!")
    return board.get_board_map()

def parse_input(turn_input):
    turn_input = turn_input.replace(" ", "")
    fromL = parse_letter_input(turn_input[0])
    fromD = parse_digit_input(turn_input[1]) 
    toL   = parse_letter_input(turn_input[2])
    toD   = parse_digit_input(turn_input[3]) 
    return [fromD, fromL, toD, toL]

def validate_input(player_input):
    pattern = re.compile(r'[A-H][1-8]\s*[A-H][1-8]\s*', re.IGNORECASE)
    return bool(pattern.match(player_input))

def validate_order(player_input, board: Board, expected_color):
    parsed_input = parse_input(player_input)
    if(expected_color == "white"):
        piece = board.get_piece(parsed_input[0], parsed_input[1])
        return piece in pieces.white_pieces
    if(expected_color == "black"):
        piece = board.get_piece(parsed_input[0], parsed_input[1])
        return piece in pieces.black_pieces
    return True

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
    turn(chessboard, "white")
    board_renderer.render_board(chessboard)
    turn(chessboard, "black")
