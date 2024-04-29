from color import Color

class Light:

    def __init__(self, position, color=Color.from_ints(255, 255, 255), intensity=1.0, attenuation=(1, 0.1, 0.01)):
        self.position = position
        self.color = color
        self.intensity = intensity
        self.attenuation = attenuation

    def attenuation_factor(self, distance):
        kc, kl, kq = self.attenuation
        return 1 / (kc + kl * distance + kq * distance ** 2)