from board.coordinates import Coordinates
from pieces.patterns.l_checker import is_l_shape
from pieces.piece import Piece
from pieces.enums.piece_icons import Piece_Icons
from pieces.enums.colors import Color

class Knight(Piece):
    icon = Piece_Icons.knight
    color: Color

    def __init__(self, color):
        self.color = color

    def validate_movement_pattern(self, from_coord: Coordinates, to_coord: Coordinates):
        if not is_l_shape(from_coord, to_coord):
            raise ValueError("Bishop can only move diagonally")