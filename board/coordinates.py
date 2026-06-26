class Coordinates:
    l: int
    d: int

    def __init__(self, l, d):
        self.l = l
        self.d = d

    def get_as_array(self):
        return [self.l, self.d]