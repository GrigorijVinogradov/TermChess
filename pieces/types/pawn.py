from board.coordinates import Coordinates
from pieces.piece import Piece
from pieces.enums.piece_icons import Piece_Icons
from pieces.enums.colors import Color

class Pawn(Piece):
    icon = Piece_Icons.pawn
    step_count = 0
    color: Color

    def __init__(self, color):
        self.color = color

    def validate_movement_pattern(self, from_coord: Coordinates, to_coord: Coordinates):
        direction = 1
        if self.color is Color.Black:
            direction = -1

        if to_coord.l == from_coord.l - 2*direction and self.step_count == 0:
            self.step_count += 1 
            return

        if to_coord.l != from_coord.l - 1*direction:
            raise ValueError("The pawn can only move one field")

        self.step_count += 1