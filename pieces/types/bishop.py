from board.board import Board
from board.coordinates import Coordinates
from pieces.collision_checker import check_collision
from pieces.patterns.diagonal_checker import get_diagonal_colliding_piece, is_diagonal
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

        check_collision(get_diagonal_colliding_piece, from_coord, to_coord, self.color)