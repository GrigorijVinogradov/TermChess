from board.colorizer import Colorizer
from board.pieces.piece_icons import Piece_Icons
from board.constants.colors import Color

class Piece():
    icon = Piece_Icons.none
    color: Color

    def __init__(self, color):
        self.color = color

    def Draw(self):
        if self.color == Color.Black:
            return Colorizer.black(self.icon.value)
        else:
            return self.icon.value