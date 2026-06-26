from board.coordinates import Coordinates
from pieces.collision_checker import check_collision
from pieces.patterns.straight_checker import get_straight_colliding_piece, is_straight
from pieces.piece import Piece
from pieces.enums.piece_icons import Piece_Icons
from pieces.enums.colors import Color

class Rook(Piece):
    icon = Piece_Icons.rook
    color: Color

    def __init__(self, color):
        self.color = color

    def validate_movement_pattern(self, from_coord: Coordinates, to_coord: Coordinates):
        if not is_straight(from_coord, to_coord):
            raise ValueError("The Rook can only move in straight lines")

        check_collision(get_straight_colliding_piece, from_coord, to_coord, self.color)