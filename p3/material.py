import numpy as np

class Material:
    def __init__(self, color, ambient, diffuse, specular):
        self.color = self.normalize_color(color=color)
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular

    def color_at(self, hit_position):
        self.color

    def normalize_color(self, color):
        return (color[0] / 255, color[1] / 255, color[2] / 255)