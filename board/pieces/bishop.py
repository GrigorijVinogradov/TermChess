from board.pieces.piece import Piece
from board.pieces.piece_icons import Piece_Icons
from board.constants.colors import Color

class Bishop(Piece):
    icon = Piece_Icons.bishop
    color: Color

    def __init__(self, color):
        self.color = color