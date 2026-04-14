class Board:
    def __init__(self):
        size = 8
        self.board_map: list[list[str]] = [['' for _ in range (size)] for _ in range (size)]

    def clear_board(self):
        for row_id, row in enumerate(self.board_map):
            for column_id, _ in enumerate(row):
                self.board_map[row_id][column_id] = ''

    def move_piece(self, fromD, fromL, toD, toL):
        from_piece = self.get_piece(fromD, fromL)
        self.set_piece(toD, toL, from_piece)
        self.set_piece(fromD, fromL, '')

    def get_piece(self, cordL, cordD):
        return self.board_map[cordL][cordD]

    def set_piece(self, cordL, cordD, piece):
        self.board_map[cordL][cordD] = piece 

    def get_board_map(self) -> list[list[str]]:
        return self.board_map