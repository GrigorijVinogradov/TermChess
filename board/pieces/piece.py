from board.colorizer import Colorizer
from board.pieces.piece_types import Piece_Types
from board.constants.colors import Color

class Piece():
    icon = Piece_Types.none
    color: Color

    def __init__(self, color):
        self.color = color

    def Draw(self):
        if self.color == Color.Black:
            return Colorizer.black(self.icon.value)
        else:
            return self.icon.value