class Coordinates:
    l: int
    d: int

    def __init__(self, l, d):
        self.l = l
        self.d = d

    def get_as_array(self):
        return [self.l, self.d]

    def to_string(self) -> str:
        letters = "ABCDEFGH"
        return letters[-self.l+1] + str(self.d-1)