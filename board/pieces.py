from termcolor import colored
from board.colorizer import Colorizer

white_square = '◼'
black_square = Colorizer.black(white_square)

white_pawn = '♙'
black_pawn = Colorizer.black(white_pawn)

white_knight = '♘'
black_knight = Colorizer.black(white_knight)

white_bishop = '♗'
black_bishop = Colorizer.black(white_bishop)

white_rook = '♖'
black_rook = Colorizer.black(white_rook)

white_queen = '♕'
black_queen = Colorizer.black(white_queen)

white_king = '♔'
black_king = Colorizer.black(white_king)

white_pieces = [ 
white_pawn,
white_knight,
white_bishop,
white_rook,
white_queen,
white_queen,
]

black_pieces = [ 
black_pawn,
black_knight,
black_bishop,
black_rook,
black_queen,
black_queen,
]

