from pieces.enums.colors import Color


class Command():
    name: str = 'basecommand'
    counts_as_turn: bool = False

    def execute_command(self, input: str, current_color: Color):
        print("Hello World!")
