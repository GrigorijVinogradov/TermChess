class Command():
    name: str = 'helloworld'
    counts_as_turn: bool = False

    def execute_command(self, _):
        print("Hello World!")
