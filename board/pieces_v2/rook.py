from board.pieces_v2.piece import Piece
from board.constants.piece_constants import Piece_Types
from board.constants.colors import Color

class Rook(Piece):
    icon = Piece_Types.rook
    color: Color

    def __init__(self, color):
        self.color = color