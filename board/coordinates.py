class Coordinates:
    l: int
    d: int

    def __init__(self, d, l):
        self.d = d
        self.l = l

    def get_as_array(self):
        return [self.d, self.l]

    def equals(self, other) -> bool:
        if isinstance(other, Coordinates):
            return self.d == other.d and self.l == other.l
        return False

    def to_string(self) -> str:
        letters = "ABCDEFGH"
        return letters[self.l] + str(abs(8-self.d))