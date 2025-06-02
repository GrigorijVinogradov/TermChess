import pieces
import board_generator

size = 8
board_map = board_generator.get_default_board()

def is_even(number):
    return number % 2 == 0

def decide_square(row, column):
    if board_map[row][column] != '':
        return board_map[row][column]
    is_row_even = is_even(row)
    return pieces.black_square if is_even(column) == is_row_even else pieces.white_square

# Main ☆*: .｡. o(≧▽≦)o .｡.:*☆

for row, i in enumerate(board_map):
    print(size-row, end=" ")
    for column, j in enumerate(i):
        square = decide_square(row, column)
        print(square, end=" ")
    print()

print("  A B C D E F G H")

