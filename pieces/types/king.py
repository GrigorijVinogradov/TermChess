from pieces.piece import Piece
from pieces.enums.piece_icons import Piece_Icons
from pieces.enums.colors import Color

class King(Piece):
    icon = Piece_Icons.king
    color: Color

    def __init__(self, color):
        self.color = color