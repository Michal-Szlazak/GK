import math
import pygame
from sphere import Sphere
from ray_tracer import RayTracer
from image import Image
from light import Light
from material import Material
from scene import Scene

colors_rgb = [
    (255, 102, 102),   # Light Red
    (255, 178, 102),   # Light Orange
    (255, 255, 102),   # Light Yellow
    (178, 255, 102),   # Light Lime
    (102, 255, 102),   # Light Green
    (102, 255, 178),   # Light Aqua
    (102, 255, 255),   # Light Cyan
    (102, 178, 255),   # Light Sky Blue
    (102, 102, 255),   # Light Blue
    (178, 102, 255),   # Light Purple
    (255, 102, 255),   # Light Magenta
    (255, 102, 178),   # Light Pink
    (255, 153, 204),   # Light Salmon
    (255, 204, 204),   # Light Peach
    (255, 204, 153),   # Light Apricot
    (255, 204, 102),   # Light Gold
    (255, 255, 102),   # Light Lemon
    (204, 255, 102),   # Light Lime Green
    (153, 255, 102),   # Light Chartreuse
    (102, 255, 102),   # Light Lime
    (102, 255, 153),   # Light Seafoam Green
    (102, 255, 255),   # Light Electric Blue
    (102, 153, 255),   # Light Periwinkle
    (178, 102, 255),   # Light Lavender
    (255, 255, 255)    # Light White
]

class Model:

    ray_tracer = RayTracer()
    image = Image(600, 600)
    light = Light((1.5, -0.5, -10), (1, 1, 1))

    spheres = []
    lights = []

    def __init__(self):
    
        material_1 = Material((255, 0, 0), 0.5, 1, 1)
        sphere1 = Sphere((0, 0, 1), 0.5, material=material_1)

        self.spheres.append(sphere1)
        self.lights.append(self.light)

        self.scene = Scene(self.spheres, self.lights)

    def print(self, window):
        
        self.ray_tracer.render(window, self.spheres, self.image, self.scene)

        # self.image.print(window)