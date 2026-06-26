from board.constants import board_constants
from board.coordinates import Coordinates
from pieces.piece import Piece

class Board:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.board_map: list[list[Piece]] = [['' for _ in range (board_constants.size)] for _ in range (board_constants.size)]
        return cls._instance

    def clear_board(self):
        for row_id, row in enumerate(self.board_map):
            for column_id, _ in enumerate(row):
                self.board_map[row_id][column_id] = ''

    def move_piece(self, from_coords: Coordinates, to_coords: Coordinates):
        from_piece: Piece = self.get_piece(from_coords)
        from_piece.validate_movement_pattern(from_coords, to_coords)
        self.set_piece(to_coords, from_piece)
        self.set_piece(from_coords, '')

    def get_piece(self, coordinates: Coordinates) -> Piece:
        return self.board_map[coordinates.d][coordinates.l]

    def set_piece(self, coordinates: Coordinates, piece):
        self.board_map[coordinates.d][coordinates.l] = piece 

    def get_board_map(self) -> list[list[Piece]]:
        return self.board_map