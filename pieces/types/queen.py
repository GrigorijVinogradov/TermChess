from board.coordinates import Coordinates
from pieces.patterns.straight_checker import is_straight
from pieces.patterns.diagonal_checker import is_diagonal
from pieces.piece import Piece
from pieces.enums.piece_icons import Piece_Icons
from pieces.enums.colors import Color

class Queen(Piece):
    icon = Piece_Icons.queen
    color: Color

    def __init__(self, color):
        self.color = color

    def validate_movement_pattern(self, from_coord: Coordinates, to_coord: Coordinates):
        if not is_diagonal(from_coord, to_coord) and not is_straight(from_coord, to_coord):
            raise ValueError("The Queen can only move diagonally or straight")