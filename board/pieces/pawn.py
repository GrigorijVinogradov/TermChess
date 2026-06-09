from board.pieces.piece import Piece
from board.pieces.piece_types import Piece_Types
from board.constants.colors import Color

class Pawn(Piece):
    icon = Piece_Types.pawn
    color: Color

    def __init__(self, color):
        self.color = color