class Command():
    name: str = 'helloworld'
    description: str = 'Base Command'
    counts_as_turn: bool = False

    def execute_command(self, _player_input):
        print("Hello World!")
