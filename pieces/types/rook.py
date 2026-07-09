from board.coordinates import Coordinates
from pieces.collision_checker import check_collision
from pieces.patterns.straight_checker import get_straight_colliding_piece, is_straight
from pieces.piece import Piece
from pieces.enums.piece_icons import Piece_Icons
from pieces.enums.colors import Color
from util.step_counter import Step_Counter

class Rook(Piece):
    icon = Piece_Icons.rook
    step_counter: Step_Counter
    color: Color

    def __init__(self, color):
        self.color = color
        self.step_counter = Step_Counter()

    def validate_movement_pattern(self, from_coord: Coordinates, to_coord: Coordinates):
        if not is_straight(from_coord, to_coord):
            raise ValueError("The Rook can only move in straight lines")

        check_collision(get_straight_colliding_piece, from_coord, to_coord, self.color)
        self.step_counter.increment_count()