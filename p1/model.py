from cube import Cube
from cuber import Cuber
import math

WHITE = (255, 255, 255)

class Model:

    models = []
    fov = 90

    aspect_ratio = 2
    rotate_x_val = 2
    rotate_y_val = 2
    rotate_z_val = 2
    move_x_val = 5
    move_y_val = 3
    move_z_val = 3

    def __init__(self):

        cube = Cuber("cube")
        block_1 = Cuber("block_1")
        block_2 = Cuber("block_2")
        block_3 = Cuber("block_3")
        block_4 = Cuber("block_4")

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

    def zoom_in(self):
        self.fov -= 1
    
    def zoom_out(self):
        self.fov += 1

    def print_vertices(self):
        for model in self.models:
            model.print_vertices()

    def print(self, window, font):
        for model in self.models:
            model.create_edges_3d()
            model.clip_edges(0.1, 1000)
            model.get_clipped_vertices()
            model.project(math.radians(self.fov), 1, 0.1, 1000)
            model.map_to_screen_space()
            model.draw_edges(window, WHITE)
