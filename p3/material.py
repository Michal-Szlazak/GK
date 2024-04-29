import numpy as np
from color import Color

class Material:
    def __init__(self, color=Color.from_ints(255, 0, 0), ambient=0.05, diffuse=1.0, specular=1.0, n=50.0, f_att=0.1):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular
        self.n = n
        self.f_att = f_att

    def color_at(self):
        return self.color