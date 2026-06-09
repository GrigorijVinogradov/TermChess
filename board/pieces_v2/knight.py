from board.pieces_v2.piece import Piece
from board.constants.piece_constants import Piece_Types
from board.constants.colors import Color

class Knight(Piece):
    icon = Piece_Types.knight
    color: Color

    def __init__(self, color):
        self.color = color