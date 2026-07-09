from board.coordinates import Coordinates

class Step_History():
    history: list[(Coordinates, Coordinates)] = []

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls.history: list[(Coordinates, Coordinates)] = []
        return cls._instance

    def add_to_history(self, from_coords: Coordinates, to_coords: Coordinates):
        self.history.append((from_coords, to_coords))

    def history_as_string(self):
        result = ''
        for entry in self.history:
            result += entry[0].to_string()
            result += entry[1].to_string()
            result += ' '

        return result