from vector import Vector

class Color(Vector):

    def __init__(self, r, g, b):
        super().__init__(r, g, b)

    @classmethod
    def from_ints(cls, r=0, g=0, b=0):
        return cls(r / 255, g / 255, b / 255)