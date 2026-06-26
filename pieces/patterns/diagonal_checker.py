from board.constants import board_constants
from board.coordinates import Coordinates

@staticmethod
def is_diagonal(from_coord: Coordinates, to_coord: Coordinates):
        from_l = from_coord.l
        from_d = from_coord.d

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