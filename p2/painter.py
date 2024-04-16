from cube import Cube
import math
import pygame

WHITE = (255, 255, 255)
GREY = (128, 128, 128)

class Painter:

    walls = []

    def create_and_add_walls(self, cube):
        cube.walls = []

        # Front wall
        cube.walls.append((cube.translated_vertices[0][:2], cube.translated_vertices[1][:2], cube.translated_vertices[3][:2], cube.translated_vertices[5][:2]))

        # Back wall
        cube.walls.append((cube.translated_vertices[8][:2], cube.translated_vertices[9][:2], cube.translated_vertices[11][:2], cube.translated_vertices[13][:2]))

        # Upper wall
        cube.walls.append((cube.translated_vertices[0][:2], cube.translated_vertices[1][:2], cube.translated_vertices[8][:2], cube.translated_vertices[9][:2]))

        # Lower wall
        cube.walls.append((cube.translated_vertices[3][:2], cube.translated_vertices[5][:2], cube.translated_vertices[11][:2], cube.translated_vertices[13][:2]))

        # Left wall
        cube.walls.append((cube.translated_vertices[0][:2], cube.translated_vertices[5][:2], cube.translated_vertices[13][:2], cube.translated_vertices[8][:2]))

        # Right wall
        cube.walls.append((cube.translated_vertices[1][:2], cube.translated_vertices[3][:2], cube.translated_vertices[9][:2], cube.translated_vertices[11][:2]))

    def paint_walls(self, cube, screen, color):
        for wall in cube.walls:
            pygame.draw.polygon(screen, color, wall, 0)

    def add_walls(self, cubes):
        for cube in cubes:
            self.create_and_add_walls(cube)

    def sort_walls(self):
        self.walls.sort(key=lambda wall: wall[0][2])


