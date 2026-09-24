from board.coordinates import Coordinates
from util.colorizer import Colorizer
from pieces.enums.piece_icons import Piece_Icons
from pieces.enums.colors import Color

class Piece():
    icon = Piece_Icons.none
    color: Color

    def __init__(self, color):
        self.color = color

    def draw(self):
        if self.color == Color.Black:
            return Colorizer.black(self.icon.value)
        else:
            return self.icon.value

    def validate_movement_pattern(self, from_coord: Coordinates, to_coord: Coordinates) -> None:
        raise ValueError("Blank Piece shouldn't move")
