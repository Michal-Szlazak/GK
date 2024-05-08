from sphere import Sphere
from ray_tracer import RayTracer
from light import Light
from material import Material
from scene import Scene
from color import Color
from vector import Vector
from point import Point

class Model:

    WIDTH = 800
    HEIGHT = 600
    camera = Vector(0, 0, -1)
    # ambient=0.2, diffuse=1.0, specular=1.0, n=50.0, f_att=0.1
    METALLIC = Material(Color.from_ints(255, 255, 255), 0.1, 0.2, 0.8, 300.0, 0.1)
    WALL = Material(Color.from_ints(255, 255, 255), 0.1, 0.8, 0.2, 5.0, 0.1)
    PLASTIC = Material(Color.from_ints(255, 255, 255), 0.1, 0.4, 0.6, 50.0, 0.1)
    WOOD = Material(Color.from_ints(184, 115, 51), 0.1, 0.6, 0.4, 25.0, 0.1)
    
    
    COPPER = Material(Color.from_ints(184, 135, 101), 0.1, 0.5, 0.5, 100.0, 0.5)

    objects = [
        # Sphere(Point(0, 0, 0), 0.5, COPPER),
        # Sphere(Point(0, 0, 0), 0.5, WALL),
        # Sphere(Point(0, 0, 0), 0.5, METALLIC),
        # Sphere(Point(0, 0, 0), 0.5, PLASTIC),
        # Sphere(Point(-0.6, -0.6, 1.5), 0.5, METALLIC),
        # Sphere(Point(0.6, -0.6, 1.5), 0.5, WALL),
        # Sphere(Point(-0.6, 0.6, 1.5), 0.5, PLASTIC),
        # Sphere(Point(0.6, 0.6, 1.5), 0.5, WOOD)
        ]
    lights = [
        Light(Point(-1, -1, -1), Color.from_ints(255, 255, 255)),
        # Light(Point(1, -1, -1), Color.from_ints(255, 255, 255))
        ]
    scene = Scene(camera, objects, lights, WIDTH, HEIGHT)

    RayTracer = RayTracer()

    def print(self, window, id):

        lights = [
            Light(Point(-1, -1, -1), Color.from_ints(255, 255, 255)),
            # Light(Point(1, -1, -1), Color.from_ints(255, 255, 255))
        ]

        if id == 1:
            self.objects = [
                Sphere(Point(0, 0, 0), 0.5, self.METALLIC),
            ]
        elif id == 2:
            self.objects = [
                Sphere(Point(0, 0, 0), 0.5, self.WALL),
            ]
        elif id == 3:
            self.objects = [
                Sphere(Point(0, 0, 0), 0.5, self.PLASTIC),
            ]
        elif id == 4:
            self.objects = [
                Sphere(Point(0, 0, 0), 0.5, self.WOOD),
            ]
        elif id == 5:
            self.objects = [
                Sphere(Point(-0.6, -0.6, 1.5), 0.5, self.METALLIC),
                Sphere(Point(0.6, -0.6, 1.5), 0.5, self.WALL),
                Sphere(Point(-0.6, 0.6, 1.5), 0.5, self.PLASTIC),
                Sphere(Point(0.6, 0.6, 1.5), 0.5, self.WOOD)
            ]
        self.scene = Scene(self.camera, self.objects, lights, self.WIDTH, self.HEIGHT)
        
        self.RayTracer.render(self.scene, window)