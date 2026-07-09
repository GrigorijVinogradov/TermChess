from board.board import Board
from board.coordinates import Coordinates
from pieces.collision_checker import check_collision, get_direct_colliding_piece
from pieces.patterns.straight_checker import get_straight_colliding_piece
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
        direction = self.determine_direction()

        if self.is_valid_two_field_step(from_coord, to_coord):
            self.step_count += 1 
            return

        if to_coord.d != from_coord.d - 1*direction:
            raise ValueError("The pawn can only move one field")

        self.validate_attack(from_coord, to_coord)
        check_collision(get_direct_colliding_piece, from_coord, to_coord, self.color)
        self.step_count += 1

    def is_valid_two_field_step(self, from_coord: Coordinates, to_coord: Coordinates) -> bool:
        direction = self.determine_direction()

        l_distance = abs(from_coord.l - to_coord.l)
        if l_distance != 0:
            raise ValueError("The pawn can only move straight forward")

        if to_coord.d == from_coord.d - 2*direction and self.step_count == 0:
            check_collision(get_straight_colliding_piece, from_coord, to_coord, self.color)
            return True

        return False

    def validate_attack(self, from_coord: Coordinates, to_coord: Coordinates):
        l_dist = abs(to_coord.l - from_coord.l)
        if l_dist > 1:
            raise ValueError("Diagonal Distance is too far")

        if l_dist == 1:
            board = Board()
            attacked_piece = board.get_piece(to_coord)
            if attacked_piece == '' or attacked_piece.color == self.color:
                raise ValueError("Can only move diagonally if attacking")

    def determine_direction(self) -> int:
        direction = 1
        if self.color is Color.Black:
            direction = -1

        return direction