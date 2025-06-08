import pieces
import os

size = 8

def is_even(number):
    return number % 2 == 0

def decide_square(board_map, row, column):
    if board_map[row][column] != '':
        return board_map[row][column]
    is_row_even = is_even(row)
    return pieces.black_square if is_even(column) == is_row_even else pieces.white_square

# Main ☆*: .｡. o(≧▽≦)o .｡.:*☆
def render_board(board_map):
    os.system('cls')
    for row, i in enumerate(board_map):
        print(size-row, end=" ")
        for column, _ in enumerate(i):
            square = decide_square(board_map, row, column)
            print(square, end=" ")
        print()
    
    print("  A B C D E F G H")
    print()
