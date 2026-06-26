class Coordinates:
    l: int
    d: int

    def __init__(self, l, d):
        self.d = l
        self.l = d

    def get_as_array(self):
        return [self.d, self.l]

    def to_string(self) -> str:
        letters = "ABCDEFGH"
        return letters[self.l] + str(abs(8-self.d))