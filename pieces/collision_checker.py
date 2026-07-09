
from board.board import Board
from board.coordinates import Coordinates
from pieces.enums.colors import Color

@staticmethod
def check_collision(collision_method, from_coord: Coordinates, to_coord: Coordinates, color: Color):
    colliding_coords = collision_method(from_coord, to_coord)
    if colliding_coords is not None:
            board = Board()
            colliding_piece = board.get_piece(colliding_coords)
            if to_coord.equals(colliding_coords) and colliding_piece.color != color:
                return

            raise ValueError(colliding_piece.draw() + " is in the way at " + colliding_coords.to_string())
    
@staticmethod
def get_direct_colliding_piece(_, to_coord):
    board = Board()
    piece = board.get_piece(to_coord)
    if piece != '':
            return to_coord