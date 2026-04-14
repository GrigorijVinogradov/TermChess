from termcolor import colored

def black(character):
    return colored(character, 'red') 

white_square = '◼'
black_square = black(white_square)

white_pawn = '♙'
black_pawn = black(white_pawn)

white_knight = '♘'
black_knight = black(white_knight)

white_bishop = '♗'
black_bishop = black(white_bishop)

white_rook = '♖'
black_rook = black(white_rook)

white_queen = '♕'
black_queen = black(white_queen)

white_king = '♔'
black_king = black(white_king)

