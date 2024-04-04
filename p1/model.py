from cube import Cube
import math

class Model:

    models = []
    fov = 90

    aspect_ratio = 1
    rotate_x_val = 1
    rotate_y_val = 1
    rotate_z_val = 1
    move_x_val = 1
    move_y_val = 1
    move_z_val = 1

    def __init__(self):

        cube = Cube("cube")
        block_1 = Cube("block_1")
        block_2 = Cube("block_2")
        block_3 = Cube("block_3")
        block_4 = Cube("block_4")

        self.models.append(cube)
        self.models.append(block_1)
        self.models.append(block_2)
        self.models.append(block_3)
        self.models.append(block_4)

    def move_x(self):
        for model in self.models:
            model.move(self.move_x_val, 0, 0)
    
    def move_x_neg(self):
        for model in self.models:
            model.move(-self.move_x_val, 0, 0)

    def move_y(self):
        for model in self.models:
            model.move(0, self.move_y_val, 0)

    def move_y_neg(self):
        for model in self.models:
            model.move(0, -self.move_y_val, 0)

    def move_z(self):
        for model in self.models:
            model.move(0, 0, self.move_z_val)

    def move_z_neg(self):
        for model in self.models:
            model.move(0, 0, -self.move_z_val)

    def rotate_x(self):
        for model in self.models:
            model.rotate(math.radians(self.rotate_x_val), 0, 0)

    def rotate_x_neg(self):
        for model in self.models:
            model.rotate(-math.radians(self.rotate_x_val), 0, 0)

    def rotate_y(self):
        for model in self.models:
            model.rotate(0, math.radians(self.rotate_y_val), 0)

    def rotate_y_neg(self):
        for model in self.models:
            model.rotate(0, -math.radians(self.rotate_y_val), 0)

    def rotate_z(self):
        for model in self.models:
            model.rotate(0, 0, math.radians(self.rotate_z_val))

    def rotate_z_neg(self):
        for model in self.models:
            model.rotate(0, 0, -math.radians(self.rotate_z_val))

    def print(self, window):
        for model in self.models:
            model.project(math.radians(self.fov), self.aspect_ratio, 1, 1000)
            model.create_edges()
            model.clip_edges()
            model.map_to_screen_space()
            model.draw_cube(window)
