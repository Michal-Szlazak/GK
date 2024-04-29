import math
import pygame
from sphere import Sphere
from ray_tracer import RayTracer
from image import Image
from light import Light
from material import Material
from scene import Scene
from color import Color
from vector import Vector
from point import Point

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

    WIDTH = 600
    HEIGHT = 600
    camera = Vector(0, 0, -1)
    objects = [
        Sphere(Point(0, 0, 0), 0.5, Material(Color.from_ints(150, 1, 1)))
        ]
    lights = [
        Light(Point(1.5, -0.5, -10.0), Color.from_ints(255, 255, 255))
        ]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)

    RayTracer = RayTracer()

    def print(self, window):
        
        self.RayTracer.render(self.scene, window)