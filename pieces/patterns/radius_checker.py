from board.coordinates import Coordinates

@staticmethod
def is_in_radius(from_coord: Coordinates, to_coord: Coordinates, radius: int):
        distance_l = abs(from_coord.d - to_coord.d)
        distance_d = abs(from_coord.l - to_coord.l)
        if distance_l > radius or distance_d > radius:
            return False
        return True