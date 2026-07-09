from board.board import Board
from board.coordinates import Coordinates
from pieces.collision_checker import check_collision
from pieces.patterns.diagonal_checker import get_diagonal_colliding_piece, is_diagonal
from pieces.patterns.radius_checker import is_in_radius
from pieces.patterns.straight_checker import get_straight_colliding_piece, is_straight
from pieces.piece import Piece
from pieces.enums.piece_icons import Piece_Icons
from pieces.enums.colors import Color
from pieces.types.rook import Rook
from util.step_counter import Step_Counter

class King(Piece):
    icon = Piece_Icons.king
    step_counter: Step_Counter
    color: Color

    def __init__(self, color):
        self.color = color
        self.step_counter = Step_Counter()

    def validate_movement_pattern(self, from_coord: Coordinates, to_coord: Coordinates):
        if not is_diagonal(from_coord, to_coord) and not is_straight(from_coord, to_coord):
            raise ValueError("The King can only move diagonally or straight")

        if self.is_castling(from_coord, to_coord):
            self.step_counter.increment_count()
            return

        if not is_in_radius(from_coord, to_coord, 1):
            raise ValueError("The King can only move one tile diagonally or straight")

        check_collision(get_straight_colliding_piece, from_coord, to_coord, self.color)
        check_collision(get_diagonal_colliding_piece, from_coord, to_coord, self.color)

        self.step_counter.increment_count()

    def is_castling(self, from_coord: Coordinates, to_coord: Coordinates):
        l_dist = from_coord.l - to_coord.l
        d_dist = from_coord.d - to_coord.d

        if d_dist != 0 or abs(l_dist) != 2:
            return False

        if self.step_counter.get_count() != 0:
            raise ValueError("Can't castle, the king has already moved previously!")

        is_king_side = l_dist < 0
        rook_from_coords: Coordinates
        rook_to_coords: Coordinates


        if is_king_side:
            rook_from_coords = Coordinates(to_coord.d, 7)
            rook_to_coords = Coordinates(to_coord.d, 5)
        else:
            rook_from_coords = Coordinates(to_coord.d, 0)
            rook_to_coords = Coordinates(to_coord.d, 3)

        board = Board()
        rook = board.get_piece(rook_from_coords)

        if not isinstance(rook, Rook):
            raise ValueError("There is no rook in Castling Position!")

        if rook.step_counter.get_count() != 0:
            raise ValueError("Can't castle, Rook has already moved previously!")

        check_collision(get_straight_colliding_piece, from_coord, to_coord, self.color)
        board.move_piece(rook_from_coords, rook_to_coords)

        return True