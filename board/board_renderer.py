from board.board import Board
from board.constants import board_constants
import os
import platform
from pieces.enums.colors import Color
from pieces.piece import Piece

def is_even(number):
    return number % 2 == 0

def decide_square(board_map, row, column):
    piece = board_map[row][column]
    if isinstance(piece, Piece):
        return piece.draw()

    is_row_even = is_even(row)
    should_be_black = is_even(column) == is_row_even
    color = Color.Black if should_be_black else Color.White
    square = Piece(color)
    return square.draw()

# Main ☆*: .｡. o(≧▽≦)o .｡.:*☆
def render_board():
    clear_screen()
    board = Board()
    board_map = board.get_board_map()
    for row, i in enumerate(board_map):
        print(board_constants.size-row, end=" ")
        for column, _ in enumerate(i):
            square = decide_square(board_map, row, column)
            print(square, end=" ")
        print()
    
    print("  A B C D E F G H")
    print()

def clear_screen():
    system = platform.system()
    if system == "Windows":
        os.system('cls')
    else:
        os.system('clear')
