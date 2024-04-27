import math
import numpy as np
from material import Material

class Sphere:

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material
    
    def hit_position(self, ray):

        origin = np.array(ray.origin)
        direction = np.array(ray.direction)
        oc = origin - self.center
        # a = direction.dot(ray.direction)
        a = 1.0
        b = 2.0 * oc.dot(ray.direction)
        c = oc.dot(oc) - self.radius * self.radius
        discriminant = b * b - 4 * a * c
        if discriminant > 0:
            dist = (-b - math.sqrt(discriminant)) / (2 * a)
            if dist > 0:
                return dist
        return None
    
    def normal(self, hit_position):
        return (hit_position - self.center) / self.radius # .normalize?
