from board.constants import board_constants
from board.coordinates import Coordinates

@staticmethod
def is_l_shape(from_coord: Coordinates, to_coord: Coordinates):
        from_l = from_coord.l
        from_d = from_coord.d

        possible_coords = [
            [from_l+2, from_d+1],
            [from_l-2, from_d-1],
            [from_l+2, from_d-1],
            [from_l-2, from_d+1],

            [from_l+1, from_d+2],
            [from_l-1, from_d-2],
            [from_l+1, from_d-2],
            [from_l-1, from_d+2]
            ]

        if (to_coord.get_as_array() in possible_coords):
                return True

        return False