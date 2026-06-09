from board.board import Board
from board.constants import board_constants
import board.pieces as pieces
import os
from board.pieces_v2.piece import Piece
from board.pieces_v2.knight import Knight

def is_even(number):
    return number % 2 == 0

def decide_square(board_map, row, column):
    piece = board_map[row][column]
    if isinstance(piece, Piece) :
        return piece.Draw()
    if board_map[row][column] != '':
        return board_map[row][column]
    is_row_even = is_even(row)
    return pieces.black_square if is_even(column) == is_row_even else pieces.white_square

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
