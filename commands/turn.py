import re

from board.board import Board
from board.coordinates import Coordinates
from commands.command import Command
from pieces.enums.colors import Color
from pieces.piece import Piece
from util.step_history import Step_History

class Turn(Command):
    name: str = 'basecommand'
    counts_as_turn: bool = True

    def execute_command(self, input: str, current_color: Color):
        board = Board()
        step_history = Step_History()
        self.validate_order(input, current_color)
        parsed_input = self.parse_input(input)
        from_coords = Coordinates(parsed_input[0], parsed_input[1]) 
        to_coords = Coordinates(parsed_input[2], parsed_input[3])
        board.move_piece(from_coords, to_coords)
        step_history.add_to_history(from_coords, to_coords)

    def parse_input(self, turn_input):
        self.validate_input(turn_input)
        turn_input = turn_input.replace(" ", "")
        fromL = self.parse_letter_input(turn_input[0])
        fromD = self.parse_digit_input(turn_input[1]) 
        toL   = self.parse_letter_input(turn_input[2])
        toD   = self.parse_digit_input(turn_input[3]) 
        return [fromD, fromL, toD, toL]

    def validate_input(self, player_input):
        pattern = re.compile(r'[A-H][1-8]\s*[A-H][1-8]\s*', re.IGNORECASE)
        if(bool(pattern.match(player_input)) == False):
            raise ValueError("Input is formatted incorrectly ([A-H][1-8] [A-H][1-8] expected)")

    def validate_order(self, player_input, expected_color):
        board = Board()
        parsed_input = self.parse_input(player_input)
        coords = Coordinates(parsed_input[0], parsed_input[1])

        piece = board.get_piece(coords)
        if not isinstance(piece, Piece):
            raise ValueError("No Piece here!")

        if piece.color != expected_color:
            raise ValueError("Played piece is not the right color")

    def parse_letter_input(self, letter):
        letter = letter.lower()
        digit = ord(letter) - 97
        return digit

    def parse_digit_input(self, digit):
        return 8 - int(digit)