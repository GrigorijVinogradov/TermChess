import numpy as np

from board.board import Board
from board.coordinates import Coordinates

@staticmethod
def is_straight(from_coord: Coordinates, to_coord: Coordinates):
        if from_coord.l != to_coord.l and from_coord.d != to_coord.d:
            return False
        return True

@staticmethod
def get_straight_colliding_piece(from_coord: Coordinates, to_coord: Coordinates) -> Coordinates|None:
    if not is_straight(from_coord, to_coord):
        return None
         
    dist = 0
    list_l = []
    list_d = []

    dist_d = from_coord.d - to_coord.d
    dist_l = from_coord.l - to_coord.l

    if(dist_d == 0 and dist_l == 0):
        raise ValueError("Piece hasnt moved!!")

    if(abs(dist_d) > 0):
        dist = abs(dist_d)
        list_l = list(get_range(from_coord.d, to_coord.d, dist_d))
        list_d = np.repeat(from_coord.l, dist).tolist()

    if(abs(dist_l) > 0):
        dist = abs(dist_l)
        list_d = list(get_range(from_coord.l, to_coord.l, dist_l))
        list_l = np.repeat(from_coord.d, dist).tolist()

    
    board = Board()
    for i in range(dist):
        coords = Coordinates(list_l[i], list_d[i])
        piece = board.get_piece(coords)
        if piece != '':
            return coords

    return None

def get_range(from_1d: int, to_1d: int, distance: int) -> range:
    step = -1 if distance > 0 else 1 
    return range(from_1d + step, to_1d + step, step)     