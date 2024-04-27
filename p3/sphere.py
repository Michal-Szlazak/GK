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
        a = np.dot(direction, direction)
        b = 2.0 * np.dot(oc, direction)
        c = np.dot(oc, oc) - self.radius * self.radius

        discriminant = b * b - 4 * a * c
        if discriminant > 0:
            sqrt_discriminant = math.sqrt(discriminant)
            # Find the smallest positive root
            root1 = (-b - sqrt_discriminant) / (2 * a)
            root2 = (-b + sqrt_discriminant) / (2 * a)
            if root1 > 0:
                return root1
            elif root2 > 0:
                return root2
        return None
    
    def normal(self, hit_position):
        return (hit_position - self.center) / np.linalg.norm(hit_position - self.center)
