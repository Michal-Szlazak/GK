from cube import Cube
from painter import Painter
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
    paint = True

    painter = Painter()

    def __init__(self):

        block_1 = Cube("objects/block_1")
        block_2 = Cube("objects/block_2")
        block_3 = Cube("objects/block_3")
        block_4 = Cube("objects/block_4")
        # pyramid = Cube("objects/pyramid")
        

        self.models.append(block_1)
        self.models.append(block_2)
        self.models.append(block_3)
        self.models.append(block_4)
        # self.models.append(pyramid)
        

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

    def change_paint_mode(self):
        print("Paint mode changed")
        self.paint = not self.paint

    def print_vertices(self):
        for model in self.models:
            model.print_vertices()

    def print(self, window):
        for model in self.models:
            model.create_edges_3d()
            model.clip_edges(100, 1000)
            model.get_clipped_vertices()
            model.project(math.radians(self.fov), 1, 0.1, 1000)
            model.map_to_screen_space()

            if self.paint:    
                self.painter.create_and_add_walls(model)
                self.painter.sort_walls()
                self.painter.paint_walls(model, window, (0, 0, 255))

            model.draw_edges(window, WHITE)
