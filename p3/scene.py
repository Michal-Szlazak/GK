

class Scene:

    def __init__(self, spheres, lights):
        self.camera = (0, 0, 0)
        self.spheres = spheres
        self.lights = lights
        self.width = 600
        self.height = 600