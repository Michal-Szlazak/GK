import numpy as np
import math
import pygame
import projection as proj

WHITE = (255, 255, 255)

class Cube:

    WIDTH = 600
    HEIGHT = 600

    vertices = np.array([[]])
    translated_vertices = np.array([[]])
    edges = []
    clipped_edges = []
    
    walls = []

    # Wczytanie danych z pliku
    def __init__(self, filename):
        
        file = open(filename, "r")
        lines = file.readlines()

        n = len(lines)

        self.translated_vertices = np.zeros((n, 4))
        self.vertices = np.zeros((n, 4))
        self.clipped_vertices = np.zeros((n, 4))

        for i in range(0, len(lines), 2):
            line = lines[i].split(" ")
            self.vertices[i] = np.array([float(line[0]), float(line[1]), float(line[2]), 1])

            line = lines[i + 1].split(" ")
            self.vertices[i + 1] = np.array([float(line[0]), float(line[1]), float(line[2]), 1])

        self.create_edges_3d()
        
    # Stworzenie krawędzi z wczytanych danych
    def create_edges_3d(self):

        self.edges = []

        for i in range(0, len(self.vertices), 2):
            self.edges.append((self.vertices[i], self.vertices[i + 1]))

    # Przycięcie krawędzi
    def clip_edges(self, near, far):
        self.clipped_edges = []
        for edge in self.edges:
            clipped_edge = self.clip_line(edge, near)
            if clipped_edge[0][0] != float('inf') and clipped_edge[1][0] != float('inf'):
                self.clipped_edges.append(clipped_edge)
        # print("Number of clipped edges: ", len(self.clipped_edges))

    # Pobranie przyciętych wierzchołków
    def get_clipped_vertices(self):
        self.clipped_vertices = []
        for edge in self.clipped_edges:
            self.clipped_vertices.append(edge[0])
            self.clipped_vertices.append(edge[1])

    # Rysowanie krawędzi
    def draw_edges(self, window, color):
        
        for i in range(0, len(self.translated_vertices), 2):
            
            pygame.draw.line(window, color, 
                             (self.translated_vertices[i][0], self.translated_vertices[i][1]),
                             (self.translated_vertices[i + 1][0], self.translated_vertices[i + 1][1]))
    
    # Przycięcie krawędzi - funkcja
    def clip_line(self, edge, near):
        
        p1 = edge[0]
        p2 = edge[1]

        if p1[2] < near and p2[2] < near:
            # print("Both points are behind the near plane")
            return (
                [np.nan, np.nan, np.nan, np.nan],
                [np.nan, np.nan, np.nan, np.nan]
                )
        
        if p1[2] < near:
            t = (near - p1[2]) / (p2[2] - p1[2])
            p1 = p1 + t * (p2 - p1)
        
        if p2[2] < near:
            t = (near - p2[2]) / (p1[2] - p2[2])
            p2 = p2 + t * (p1 - p2)
        
        return (p1, p2)

    # Przesunięcie wierzchołków
    def move(self, x, y, z):
        self.vertices = np.add(self.vertices, np.array([x, y, z, 0]))

    # Obrót
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
            
    # Rzutowanie
    def project(self, fov, aspect_ratio, near, far):
        proj_matrix = proj.perspective_projection_matrix(fov, aspect_ratio, near, far)

        for i in range(len(self.clipped_vertices)):
            self.translated_vertices[i] = proj.perspective_divide(proj_matrix, self.clipped_vertices[i])
    
    # Mapowanie do przestrzeni ekranu
    def map_to_screen_space(self):
        for i in range(len(self.translated_vertices)):
            if(np.isnan(self.translated_vertices[i][0]) or np.isnan(self.translated_vertices[i][1])):
                continue
            self.translated_vertices[i] = proj.map_to_screen_space(self.translated_vertices[i], self.WIDTH, self.HEIGHT)