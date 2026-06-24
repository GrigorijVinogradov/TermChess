from board.coordinates import Coordinates

@staticmethod
def is_straight(from_coord: Coordinates, to_coord: Coordinates):
        if from_coord.d != to_coord.d and from_coord.l != to_coord.l:
            return False
        return True