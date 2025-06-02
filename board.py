import pieces

size = 8
board_map = [['' for _ in range (size)] for _ in range (size)]

def initialize_board():
    initialize_pawns()
    initialize_rooks()
    initialize_knights()
    initialize_bishops()
    initialize_royals()

def initialize_symmetrical_pieces(row, column, piece):
    board_map[row][size-column-1] = piece
    board_map[row][column] = piece

def initialize_pawns():
    for column, _ in enumerate(board_map):
        board_map[1][column] = pieces.black_pawn 
        board_map[6][column] = pieces.white_pawn

def initialize_rooks():
    initialize_symmetrical_pieces(0, 0, pieces.black_rook)
    initialize_symmetrical_pieces(7, 0, pieces.white_rook)

def initialize_knights():
    initialize_symmetrical_pieces(0, 1, pieces.black_knight)
    initialize_symmetrical_pieces(7, 1, pieces.white_knight)

def initialize_bishops():
    initialize_symmetrical_pieces(0, 2, pieces.black_bishop)
    initialize_symmetrical_pieces(7, 2, pieces.white_bishop)

def initialize_royals():
    board_map[0][3] = pieces.black_queen
    board_map[0][4] = pieces.black_king
    board_map[7][3] = pieces.white_queen
    board_map[7][4] = pieces.white_king

def is_even(number):
    return number % 2 == 0

def decide_square(row, column):
    if board_map[row][column] != '':
        return board_map[row][column]
    is_row_even = is_even(row)
    return pieces.black_square if is_even(column) == is_row_even else pieces.white_square

# Main ☆*: .｡. o(≧▽≦)o .｡.:*☆

initialize_board()
for row, i in enumerate(board_map):
    print(size-row, end=" ")
    for column, j in enumerate(i):
        square = decide_square(row, column)
        print(square, end=" ")
    print()

print("  A B C D E F G H")

