from board.pieces.piece import Piece
from board.pieces.enums.piece_icons import Piece_Icons
from board.pieces.enums.colors import Color

class Pawn(Piece):
    icon = Piece_Icons.pawn
    color: Color

    def __init__(self, color):
        self.color = color