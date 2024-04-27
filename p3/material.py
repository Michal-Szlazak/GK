

class Material:
    def __init__(self, color, ambient, diffuse, specular):
        self.color = color
        self.ambient = ambient
        self.diffuse = diffuse
        self.specular = specular

    def color_at(self, hit_position):
        self.color