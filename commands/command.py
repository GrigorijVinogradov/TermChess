from pieces.enums.colors import Color


class Command():
    name: str = 'helloworld'
    counts_as_turn: bool = False

    def execute_command(self, input: str):
        print("Hello World!")
