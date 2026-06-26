from board.coordinates import Coordinates
from pieces.collision_checker import check_collision
from pieces.patterns.diagonal_checker import get_diagonal_colliding_piece, is_diagonal
from pieces.patterns.radius_checker import is_in_radius
from pieces.patterns.straight_checker import get_straight_colliding_piece, is_straight
from pieces.piece import Piece
from pieces.enums.piece_icons import Piece_Icons
from pieces.enums.colors import Color

class King(Piece):
    icon = Piece_Icons.king
    color: Color

    def __init__(self, color):
        self.color = color

    def validate_movement_pattern(self, from_coord: Coordinates, to_coord: Coordinates):
        if not is_diagonal(from_coord, to_coord) and not is_straight(from_coord, to_coord):
            raise ValueError("The King can only move diagonally or straight")

        if not is_in_radius(from_coord, to_coord, 1):
            raise ValueError("The King can only move one tile diagonally or straight")

        check_collision(get_straight_colliding_piece, from_coord, to_coord, self.color)
        check_collision(get_diagonal_colliding_piece, from_coord, to_coord, self.color)