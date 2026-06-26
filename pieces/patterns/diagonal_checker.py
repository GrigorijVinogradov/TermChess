from board.board import Board
from board.constants import board_constants
from board.coordinates import Coordinates

@staticmethod
def is_diagonal(from_coord: Coordinates, to_coord: Coordinates):
        from_l = from_coord.d
        from_d = from_coord.l

        for i in range(1, board_constants.size+1, 1):
            possible_coords = [
                [from_l+i, from_d+i],
                [from_l-i, from_d-i],
                [from_l+i, from_d-i],
                [from_l-i, from_d+i]
            ]

            if (to_coord.get_as_array() in possible_coords):
                return True

        return False

@staticmethod
def get_diagonal_colliding_piece(from_coord: Coordinates, to_coord: Coordinates) -> Coordinates|None:
    if not is_diagonal(from_coord, to_coord):
       return None
         
    dist_l = from_coord.d - to_coord.d
    range_l = get_range(from_coord.d, to_coord.d, dist_l)

    dist_d = from_coord.l - to_coord.l
    range_d = get_range(from_coord.l, to_coord.l, dist_d)

    length = abs(min(dist_l, dist_d))

    board = Board()
    for i in range(length):
        d = range_d[i]
        l = range_l[i]
        coords = Coordinates(l, d)
        piece = board.get_piece(Coordinates(l, d))
        if piece != '':
            return coords

    return None

def get_range(from_1d: int, to_1d: int, distance: int) -> range:
    step = -1 if distance > 0 else 1 
    return range(from_1d + step, to_1d + step, step)     