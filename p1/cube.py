import pygame
import numpy as np
import math

WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

LIGHT_BLUE = (103, 216, 200)
LIGHT_GREEN = (144, 238, 144)

class Cube:

    vertices = np.array([[]])
    translated_vertices = np.array([[]])
    edges = []

    near = 0.2

    
    def __init__(self, filename):
        file = open(filename, "r")
        lines = file.readlines()
        self.translated_vertices = np.zeros((len(lines), 4))
        self.vertices = np.zeros((len(lines), 4))

        for i in range(len(lines)):
            line = lines[i].split(" ")
            self.vertices[i] = np.array([float(line[0]), float(line[1]), float(line[2]), 1])

    def print_vertices(self):

        print("translated vertices")
        for vertex in self.translated_vertices:
            print(vertex)
        print("")

        print("Vertices:")
        for vertex in self.vertices:
            print(vertex)
        print("")

        print("Edges:")
        for edge in self.edges:
            print(edge)
        print("")

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

    def clip_edges(self):
        self.edges[0] = self.clip_line(self.edges[0][0], self.edges[0][1])
        self.edges[1] = self.clip_line(self.edges[1][0], self.edges[1][1])
        self.edges[2] = self.clip_line(self.edges[2][0], self.edges[2][1])
        self.edges[3] = self.clip_line(self.edges[3][0], self.edges[3][1])

        self.edges[4] = self.clip_line(self.edges[4][0], self.edges[4][1])
        self.edges[5] = self.clip_line(self.edges[5][0], self.edges[5][1])
        self.edges[6] = self.clip_line(self.edges[6][0], self.edges[6][1])
        self.edges[7] = self.clip_line(self.edges[7][0], self.edges[7][1])

        self.edges[8] = self.clip_line(self.edges[8][0], self.edges[8][1])
        self.edges[9] = self.clip_line(self.edges[9][0], self.edges[9][1])
        self.edges[10] = self.clip_line(self.edges[10][0], self.edges[10][1])
        self.edges[11] = self.clip_line(self.edges[11][0], self.edges[11][1])

    def rotate_cube(self, angle_x, angle_y, angle_z):
        self.rotate(angle_x, angle_y, angle_z)
    
    def draw_cube(self, window):
        for edge in self.edges:
            if edge[0] is not None and edge[1] is not None:
                pygame.draw.line(window, WHITE, edge[0][:2], edge[1][:2])

    def clip_line(self, v1, v2):

        if v1 is None or v2 is None:
            return None, None

        result1 = v1
        result2 = v2

        if v1[3] < self.near and v2[3] < self.near:
            return None, None

        if v1[3] < self.near:

            x1, y1, z1, w1 = v2
            x2, y2, z2, w2 = v1
            near = self.near

            n = (w1 - near) / (w1 - w2)
            xc = (n * x1) + ((1-n) * x2)
            yc = (n * y1) + ((1-n) * y2)
            zc = (n * z1) + ((1-n) * z2)
            wc = near
            result1 = [xc, yc, zc, wc]


        if v2[3] < self.near:
            
            x1, y1, z1, w1 = v1
            x2, y2, z2, w2 = v2
            near = self.near

            n = (w1 - near) / (w1 - w2)
            xc = (n * x1) + ((1-n) * x2)
            yc = (n * y1) + ((1-n) * y2)
            zc = (n * z1) + ((1-n) * z2)
            wc = near
            result2 = [xc, yc, zc, wc]
        
        return result1, result2
    
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
        proj_matrix = perspective_projection_matrix(fov, aspect_ratio, near, far)

        for i in range(len(self.vertices)):
            self.translated_vertices[i] = perspective_divide(proj_matrix, self.vertices[i])
    
    def map_to_screen_space(self):
        for i in range(len(self.translated_vertices)):
            self.translated_vertices[i] = map_to_screen_space(self.translated_vertices[i])

    def move(self, x, y, z):
        self.vertices = np.add(self.vertices, np.array([x, y, z, 0]))


def perspective_projection_matrix(fov, aspect_ratio, near, far):
    f = 1 / math.tan(fov / 2)

    return np.array([
        [f / aspect_ratio, 0, 0, 0],
        [0, f, 0, 0],
        [0, 0, far / (far - near), (far * near) / (near - far)],
        [0, 0, 1, 0]
    ])

def perspective_divide(perspective_projection_matrix, v):
    v = np.dot(perspective_projection_matrix, v)

    w = math.fabs(v[3])

    if v[3] == 0:
        return v

    v = np.array(v)
    return [v[0] / w, v[1] / w, v[2] / w, v[3]]

def map_to_screen_space(v):
    return (v[0] * WIDTH / 2 + WIDTH / 2, v[1] * HEIGHT / 2 + HEIGHT / 2, v[2], v[3])