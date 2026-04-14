from board import board_constants
from board.board import Board
import board.pieces as pieces

def initialize_board(board: Board):
    initialize_pawns(board)
    initialize_rooks(board)
    initialize_knights(board)
    initialize_bishops(board)
    initialize_royals(board)

def initialize_symmetrical_pieces(board: Board, row, column, piece):
    board.set_piece(row, board_constants.size-column-1, piece)
    board.set_piece(row, column, piece)

def initialize_pawns(board: Board):
    for column, _ in enumerate(board.get_board_map()):
        board.set_piece(1, column, pieces.black_pawn)
        board.set_piece(6, column, pieces.white_pawn)

def initialize_rooks(board: Board):
    initialize_symmetrical_pieces(board, 0, 0, pieces.black_rook)
    initialize_symmetrical_pieces(board, 7, 0, pieces.white_rook)

def initialize_knights(board: Board):
    initialize_symmetrical_pieces(board, 0, 1, pieces.black_knight)
    initialize_symmetrical_pieces(board, 7, 1, pieces.white_knight)

def initialize_bishops(board: Board):
    initialize_symmetrical_pieces(board, 0, 2, pieces.black_bishop)
    initialize_symmetrical_pieces(board, 7, 2, pieces.white_bishop)

def initialize_royals(board: Board):
    board.set_piece(0, 3, pieces.black_queen)
    board.set_piece(0, 4, pieces.black_king)
    board.set_piece(7, 3, pieces.white_queen)
    board.set_piece(7, 4, pieces.white_king)