from board.board import Board
from board.constants import board_constants
import os
from board.pieces.enums.colors import Color
from board.pieces.piece import Piece

def is_even(number):
    return number % 2 == 0

def decide_square(board_map, row, column):
    piece = board_map[row][column]
    if isinstance(piece, Piece):
        return piece.Draw()

    is_row_even = is_even(row)
    should_be_black = is_even(column) == is_row_even
    color = Color.Black if should_be_black else Color.White
    square = Piece(color)
    return square.Draw()

# Main ☆*: .｡. o(≧▽≦)o .｡.:*☆
def render_board(board: Board):
    os.system('cls')
    board_map = board.get_board_map()
    for row, i in enumerate(board_map):
        print(board_constants.size-row, end=" ")
        for column, _ in enumerate(i):
            square = decide_square(board_map, row, column)
            print(square, end=" ")
        print()
    
    print("  A B C D E F G H")
    print()
