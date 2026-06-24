import copy

from board.constants import board_constants
from board.board import Board
from board.coordinates import Coordinates
from pieces.enums.colors import Color
from pieces.types.pawn import Pawn 
from pieces.types.rook import Rook 
from pieces.types.knight import Knight 
from pieces.types.bishop import Bishop 
from pieces.types.queen import Queen 
from pieces.types.king import King 

def initialize_board():
    initialize_pawns()
    initialize_rooks()
    initialize_knights()
    initialize_bishops()
    initialize_queens()
    initialize_kings()

def initialize_symmetrical_pieces(coords: Coordinates, piece):
    board = Board()
    opposite_coords = Coordinates(coords.l, board_constants.size-coords.d-1)
    board.set_piece(coords, piece)
    board.set_piece(opposite_coords, piece)

def initialize_pawns():
    board = Board()
    white_pawn = Pawn(Color.White)
    black_pawn = Pawn(Color.Black)
    for column, _ in enumerate(board.get_board_map()):
        coords_white = Coordinates(6, column)
        coords_black = Coordinates(1, column)
        board.set_piece(coords_white, copy.deepcopy(white_pawn))
        board.set_piece(coords_black, copy.deepcopy(black_pawn))

def initialize_rooks():
    white_rook = Rook(Color.White)
    black_rook = Rook(Color.Black)

    white_coords = Coordinates(7, 0)
    black_coords = Coordinates(0, 0)

    initialize_symmetrical_pieces(white_coords, white_rook)
    initialize_symmetrical_pieces(black_coords, black_rook)

def initialize_knights():
    white_knight = Knight(Color.White)
    black_knight = Knight(Color.Black)

    white_coords = Coordinates(7, 1)
    black_coords = Coordinates(0, 1)

    initialize_symmetrical_pieces(white_coords, white_knight)
    initialize_symmetrical_pieces(black_coords, black_knight)

def initialize_bishops():
    white_bishop = Bishop(Color.White)
    black_bishop = Bishop(Color.Black)

    white_coords = Coordinates(7, 2)
    black_coords = Coordinates(0, 2)

    initialize_symmetrical_pieces(white_coords, white_bishop)
    initialize_symmetrical_pieces(black_coords, black_bishop)

def initialize_queens():
    board = Board()
    white_queen = Queen(Color.White)
    black_queen = Queen(Color.Black)

    white_queen_coords = Coordinates(7, 3)
    black_queen_coords = Coordinates(0, 3)

    board.set_piece(white_queen_coords, white_queen)
    board.set_piece(black_queen_coords, black_queen)

def initialize_kings():
    board = Board()
    white_king = King(Color.White)
    black_king = King(Color.Black)

    white_king_coords = Coordinates(7, 4)
    black_king_coords = Coordinates(0, 4)

    board.set_piece(white_king_coords, white_king)
    board.set_piece(black_king_coords, black_king)