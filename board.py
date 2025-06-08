import pieces

size = 8
board_map = [['' for _ in range (size)] for _ in range (size)]

def clear_board():
    for row_id, row in enumerate(board_map):
        for column_id, _ in enumerate(row):
            board_map[row_id][column_id] = ''

def move_piece(fromD, fromL, toD, toL):
    from_piece = get_piece(fromD, fromL)
    set_piece(toD, toL, from_piece)
    set_piece(fromD, fromL, '')

def get_piece(cordL, cordD):
    return board_map[cordL][cordD]

def set_piece(cordL, cordD, piece):
    board_map[cordL][cordD] = piece 

def get_current_board():
    return board_map

def get_default_board():
    clear_board()
    initialize_board()
    return board_map

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
