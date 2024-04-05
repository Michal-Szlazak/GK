import pygame
import numpy as np
import math
import projection as proj

WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

LIGHT_BLUE = (103, 216, 200)
LIGHT_GREEN = (144, 238, 144)

class Cube:

    WIDTH = 600
    HEIGHT = 600

    vertices = np.array([[]])
    clipped_vertices = np.array([[]])
    translated_vertices = np.array([[]])
    edges = []

    near = 0
    
    def __init__(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        self.translated_vertices = np.zeros((len(lines), 4))
        self.vertices = np.zeros((len(lines), 4))
        self.clipped_vertices = np.zeros((len(lines), 4))

        for i in range(len(lines)):
            line = lines[i].split(" ")
            self.vertices[i] = np.array([float(line[0]), float(line[1]), float(line[2]), 1])

    def draw_coordinates(self, window, font):

        for vertex in self.translated_vertices:
            #only whole numbers
            x = vertex[0]
            y = vertex[1]
            z = vertex[2]

            if math.isnan(x):
                x = 0
            if math.isnan(y):
                y = 0
            if math.isnan(z):
                z = 0

            text = font.render(f"({int(x)}, {int(y)}, {int(z)})", True, WHITE)
            window.blit(text, (vertex[0], vertex[1]))
            

    def print_vertices(self):

        print("translated vertices")
        for vertex in self.translated_vertices:
            print(vertex)
        print("")

        # print("Vertices:")
        # for vertex in self.vertices:
        #     print(vertex)
        # print("")

        # print("Clipped vertices")
        # for vertex in self.clipped_vertices:
        #     print(vertex)
        # print("")

        # print("Edges:")
        # for edge in self.edges:
        #     print(edge)
        # print("")

    def create_edges(self):
        self.edges = []

        self.edges.append((self.translated_vertices[0], self.translated_vertices[1]))
        self.edges.append((self.translated_vertices[1], self.translated_vertices[2]))
        self.edges.append((self.translated_vertices[2], self.translated_vertices[3]))
        self.edges.append((self.translated_vertices[3], self.translated_vertices[0]))

        self.edges.append((self.translated_vertices[4], self.translated_vertices[5]))
        self.edges.append((self.translated_vertices[5], self.translated_vertices[6]))
        self.edges.append((self.translated_vertices[6], self.translated_vertices[7]))
        self.edges.append((self.translated_vertices[7], self.translated_vertices[4]))
                          
        self.edges.append((self.translated_vertices[0], self.translated_vertices[4]))
        self.edges.append((self.translated_vertices[1], self.translated_vertices[5]))
        self.edges.append((self.translated_vertices[2], self.translated_vertices[6]))
        self.edges.append((self.translated_vertices[3], self.translated_vertices[7]))

    def rotate_cube(self, angle_x, angle_y, angle_z):
        self.rotate(angle_x, angle_y, angle_z)
    
    def draw_cube(self, window, font):
        for edge in self.edges:
            if edge[0] is not None and edge[1] is not None:
                pygame.draw.line(window, WHITE, edge[0][:2], edge[1][:2])
        
        self.draw_coordinates(window, font)
    
    def rotate(self, angle_x, angle_y, angle_z):
        rotation_matrix_x = np.array([
            [1, 0, 0, 0],
            [0, math.cos(angle_x), -math.sin(angle_x), 0],
            [0, math.sin(angle_x), math.cos(angle_x), 0],
            [0, 0, 0, 1]
        ])

        rotation_matrix_y = np.array([
            [math.cos(angle_y), 0, math.sin(angle_y), 0],
            [0, 1, 0, 0],
            [-math.sin(angle_y), 0, math.cos(angle_y), 0],
            [0, 0, 0, 1]
        ])

        rotation_matrix_z = np.array([
            [math.cos(angle_z), -math.sin(angle_z), 0, 0],
            [math.sin(angle_z), math.cos(angle_z), 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 1]
        ])

        rotation_matrix = np.dot(rotation_matrix_x, rotation_matrix_y)
        rotation_matrix = np.dot(rotation_matrix, rotation_matrix_z)

        for i in range(len(self.vertices)):
            self.vertices[i] = np.dot(rotation_matrix, self.vertices[i])

    def project(self, fov, aspect_ratio, near, far):
        proj_matrix = proj.perspective_projection_matrix(fov, aspect_ratio, near, far)

        for i in range(len(self.clipped_vertices)):
            self.translated_vertices[i] = proj.perspective_divide(proj_matrix, self.clipped_vertices[i])
    
    def map_to_screen_space(self):
        for i in range(len(self.translated_vertices)):
            self.translated_vertices[i] = proj.map_to_screen_space(self.translated_vertices[i], self.WIDTH, self.HEIGHT)

    def move(self, x, y, z):
        self.vertices = np.add(self.vertices, np.array([x, y, z, 0]))

    def clip_line(self, p1, p2):

        result1, result2 = p1, p2

        if p1[2] < self.near and p2[2] < self.near:
            return (None, None)
        
        if p1[2] < self.near:
            result1 = [p1[0], p1[1], self.near, p1[3]]

        if p2[2] < self.near:
            result2 = [p2[0], p2[1], self.near, p2[3]]

        return (result1, result2)
    
    def clip_edges(self):
        
        self.clipped_vertices = self.vertices.copy()

        (self.clipped_vertices[0], self.clipped_vertices[1]) = self.clip_line(self.vertices[0], self.vertices[1])
        (self.clipped_vertices[1], self.clipped_vertices[2]) = self.clip_line(self.vertices[1], self.vertices[2])
        (self.clipped_vertices[2], self.clipped_vertices[3]) = self.clip_line(self.vertices[2], self.vertices[3])
        (self.clipped_vertices[3], self.clipped_vertices[0]) = self.clip_line(self.vertices[3], self.vertices[0])

        (self.clipped_vertices[4], self.clipped_vertices[5]) = self.clip_line(self.vertices[4], self.vertices[5])
        (self.clipped_vertices[5], self.clipped_vertices[6]) = self.clip_line(self.vertices[5], self.vertices[6])
        (self.clipped_vertices[6], self.clipped_vertices[7]) = self.clip_line(self.vertices[6], self.vertices[7])
        (self.clipped_vertices[7], self.clipped_vertices[4]) = self.clip_line(self.vertices[7], self.vertices[4])

        (self.clipped_vertices[0], self.clipped_vertices[4]) = self.clip_line(self.vertices[0], self.vertices[4])
        (self.clipped_vertices[1], self.clipped_vertices[5]) = self.clip_line(self.vertices[1], self.vertices[5])
        (self.clipped_vertices[2], self.clipped_vertices[6]) = self.clip_line(self.vertices[2], self.vertices[6])
        (self.clipped_vertices[3], self.clipped_vertices[7]) = self.clip_line(self.vertices[3], self.vertices[7])