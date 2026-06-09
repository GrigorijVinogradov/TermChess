from board.constants import board_constants
from board.board import Board
from board.constants.colors import Color
from board.pieces_v2.pawn import Pawn 
from board.pieces_v2.rook import Rook 
from board.pieces_v2.knight import Knight 
from board.pieces_v2.bishop import Bishop 
from board.pieces_v2.queen import Queen 
from board.pieces_v2.king import King 

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
    white_pawn = Pawn(Color.White)
    black_pawn = Pawn(Color.Black)
    for column, _ in enumerate(board.get_board_map()):
        board.set_piece(1, column, black_pawn)
        board.set_piece(6, column, white_pawn)

def initialize_rooks(board: Board):
    white_rook = Rook(Color.White)
    black_rook = Rook(Color.Black)
    initialize_symmetrical_pieces(board, 0, 0, black_rook.Draw())
    initialize_symmetrical_pieces(board, 7, 0, white_rook.Draw())

def initialize_knights(board: Board):
    white_knight = Knight(Color.White)
    black_knight = Knight(Color.Black)
    initialize_symmetrical_pieces(board, 0, 1, black_knight)
    initialize_symmetrical_pieces(board, 7, 1, white_knight)

def initialize_bishops(board: Board):
    white_bishop = Bishop(Color.White)
    black_bishop = Bishop(Color.Black)
    initialize_symmetrical_pieces(board, 0, 2, black_bishop)
    initialize_symmetrical_pieces(board, 7, 2, white_bishop)

def initialize_royals(board: Board):
    white_queen = Queen(Color.White)
    black_queen = Queen(Color.Black)
    white_king = King(Color.White)
    black_king = King(Color.Black)
    board.set_piece(0, 3, black_queen)
    board.set_piece(0, 4, black_king)
    board.set_piece(7, 3, white_queen)
    board.set_piece(7, 4, white_king)