
class Phong:

    def diffuse(self, light, normal):
        return light.dot(normal)