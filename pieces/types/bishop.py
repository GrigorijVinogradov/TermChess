from board.coordinates import Coordinates
from pieces.patterns.diagonal_checker import is_diagonal
from pieces.piece import Piece
from pieces.enums.piece_icons import Piece_Icons
from pieces.enums.colors import Color

class Bishop(Piece):
    icon = Piece_Icons.bishop
    color: Color

    def __init__(self, color):
        self.color = color

    def validate_movement_pattern(self, from_coord: Coordinates, to_coord: Coordinates):
        if not is_diagonal(from_coord, to_coord):
            raise ValueError("Bishop can only move diagonally")