from board.constants import board_constants
from board.pieces_v2.piece import Piece

class Board:
    def __init__(self):
        self.board_map: list[list[Piece]] = [['' for _ in range (board_constants.size)] for _ in range (board_constants.size)]

    def clear_board(self):
        for row_id, row in enumerate(self.board_map):
            for column_id, _ in enumerate(row):
                self.board_map[row_id][column_id] = ''

    def move_piece(self, fromD, fromL, toD, toL):
        from_piece = self.get_piece(fromD, fromL)
        self.set_piece(toD, toL, from_piece)
        self.set_piece(fromD, fromL, '')

    def get_piece(self, cordL, cordD) -> Piece:
        return self.board_map[cordL][cordD]

    def set_piece(self, cordL, cordD, piece):
        self.board_map[cordL][cordD] = piece 

    def get_board_map(self) -> list[list[Piece]]:
        return self.board_map