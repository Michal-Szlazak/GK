from cube import Cube
import math
import pygame
import numpy as np

WHITE = (255, 255, 255)
GREY = (128, 128, 128)

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
]



class Painter:

    walls = []
    intersection_points = []
    intersection_lines = []
    cut_intersection_lines = {}
    intersection_points_grouped_by_y = {}
    intersection_lines_grouped_by_y = {}

    def clear(self):
        self.walls = []
        self.intersection_points = []
        self.intersection_lines = []
        self.cut_intersection_lines = {}
        self.intersection_points_grouped_by_y = {}
        self.intersection_lines_grouped_by_y = {}

    def create_5_edge_front_wall(self, cube):

        vertices = []
        final_vertices = []
        
        if(np.array_equal(cube.translated_vertices[1], cube.translated_vertices[2]) == False):
            # self.walls.append((cube.translated_vertices[0], cube.translated_vertices[1], cube.translated_vertices[2], cube.translated_vertices[3], cube.translated_vertices[5]))
            
            vertices.append(cube.translated_vertices[0])
            vertices.append(cube.translated_vertices[1])
            vertices.append(cube.translated_vertices[2])
            vertices.append(cube.translated_vertices[3])
            vertices.append(cube.translated_vertices[5])

        elif (np.array_equal(cube.translated_vertices[3], cube.translated_vertices[4]) == False):
            # self.walls.append((cube.translated_vertices[0], cube.translated_vertices[1], cube.translated_vertices[3], cube.translated_vertices[4], cube.translated_vertices[5]))

            vertices.append(cube.translated_vertices[0])
            vertices.append(cube.translated_vertices[1])
            vertices.append(cube.translated_vertices[3])
            vertices.append(cube.translated_vertices[4])
            vertices.append(cube.translated_vertices[5])
            
        elif (np.array_equal(cube.translated_vertices[5], cube.translated_vertices[6]) == False):
            # self.walls.append((cube.translated_vertices[0], cube.translated_vertices[1], cube.translated_vertices[3], cube.translated_vertices[5], cube.translated_vertices[6]))
            
            vertices.append(cube.translated_vertices[0])
            vertices.append(cube.translated_vertices[1])
            vertices.append(cube.translated_vertices[3])
            vertices.append(cube.translated_vertices[5])
            vertices.append(cube.translated_vertices[6])


        elif (np.array_equal(cube.translated_vertices[7], cube.translated_vertices[0]) == False):
            # self.walls.append((cube.translated_vertices[0], cube.translated_vertices[1], cube.translated_vertices[3], cube.translated_vertices[5], cube.translated_vertices[7]))
            
            vertices.append(cube.translated_vertices[0])
            vertices.append(cube.translated_vertices[1])
            vertices.append(cube.translated_vertices[3])
            vertices.append(cube.translated_vertices[5])
            vertices.append(cube.translated_vertices[7])

        else:
            # self.walls.append((cube.translated_vertices[0], cube.translated_vertices[1], cube.translated_vertices[3], cube.translated_vertices[5]))
            vertices.append(cube.translated_vertices[0])
            vertices.append(cube.translated_vertices[1])
            vertices.append(cube.translated_vertices[3])
            vertices.append(cube.translated_vertices[5])

        for vertex in vertices:
            if np.isnan(vertex[0]):
                continue
            final_vertices.append(vertex)

        self.walls.append(tuple(final_vertices))

    def create_5_edge_back_wall(self, cube):

        vertices = []
        final_vertices = []
        
        if(np.array_equal(cube.translated_vertices[9], cube.translated_vertices[10]) == False):
            # self.walls.append((cube.translated_vertices[8], cube.translated_vertices[9], cube.translated_vertices[10], cube.translated_vertices[11], cube.translated_vertices[13]))

            vertices.append(cube.translated_vertices[8])
            vertices.append(cube.translated_vertices[9])
            vertices.append(cube.translated_vertices[10])
            vertices.append(cube.translated_vertices[11])
            vertices.append(cube.translated_vertices[13])

        elif(np.array_equal(cube.translated_vertices[11], cube.translated_vertices[12]) == False):
            # self.walls.append((cube.translated_vertices[8], cube.translated_vertices[9], cube.translated_vertices[11], cube.translated_vertices[12], cube.translated_vertices[13]))

            vertices.append(cube.translated_vertices[8])
            vertices.append(cube.translated_vertices[9])
            vertices.append(cube.translated_vertices[11])
            vertices.append(cube.translated_vertices[12])
            vertices.append(cube.translated_vertices[13])

        elif(np.array_equal(cube.translated_vertices[13], cube.translated_vertices[14]) == False):
            self.walls.append((cube.translated_vertices[8], cube.translated_vertices[9], cube.translated_vertices[11], cube.translated_vertices[13], cube.translated_vertices[14]))
        
            vertices.append(cube.translated_vertices[8])
            vertices.append(cube.translated_vertices[9])
            vertices.append(cube.translated_vertices[11])
            vertices.append(cube.translated_vertices[13])
            vertices.append(cube.translated_vertices[14])

        elif(np.array_equal(cube.translated_vertices[15], cube.translated_vertices[8]) == False):
            # self.walls.append((cube.translated_vertices[15], cube.translated_vertices[8], cube.translated_vertices[9], cube.translated_vertices[11], cube.translated_vertices[13]))

            vertices.append(cube.translated_vertices[15])
            vertices.append(cube.translated_vertices[8])
            vertices.append(cube.translated_vertices[9])
            vertices.append(cube.translated_vertices[11])
            vertices.append(cube.translated_vertices[13])

        else:
            # self.walls.append((cube.translated_vertices[8], cube.translated_vertices[9], cube.translated_vertices[11], cube.translated_vertices[13]))

            vertices.append(cube.translated_vertices[8])
            vertices.append(cube.translated_vertices[9])
            vertices.append(cube.translated_vertices[11])
            vertices.append(cube.translated_vertices[13])

        for vertex in vertices:
            if np.isnan(vertex[0]):
                continue
            final_vertices.append(vertex)

        self.walls.append(tuple(final_vertices))


    def create_5_edge_right_wall(self, cube):

        vertices = []
        final_vertices = []

        if(np.array_equal(cube.translated_vertices[2], cube.translated_vertices[18]) == False):
            # self.walls.append((cube.translated_vertices[3], cube.translated_vertices[2], cube.translated_vertices[19], cube.translated_vertices[9], cube.translated_vertices[11]))
            vertices.append(cube.translated_vertices[3])
            vertices.append(cube.translated_vertices[2])
            vertices.append(cube.translated_vertices[18])
            vertices.append(cube.translated_vertices[19])
            vertices.append(cube.translated_vertices[11])

            
        elif (np.array_equal(cube.translated_vertices[19], cube.translated_vertices[10]) == False):
            # self.walls.append((cube.translated_vertices[3], cube.translated_vertices[2], cube.translated_vertices[19], cube.translated_vertices[10], cube.translated_vertices[11]))
            vertices.append(cube.translated_vertices[3])
            vertices.append(cube.translated_vertices[2])
            vertices.append(cube.translated_vertices[19])
            vertices.append(cube.translated_vertices[10])
            vertices.append(cube.translated_vertices[11])
            
        elif (np.array_equal(cube.translated_vertices[11], cube.translated_vertices[21]) == False):
            # self.walls.append((cube.translated_vertices[3], cube.translated_vertices[2], cube.translated_vertices[19], cube.translated_vertices[11] , cube.translated_vertices[21]))
            vertices.append(cube.translated_vertices[3])
            vertices.append(cube.translated_vertices[2])
            vertices.append(cube.translated_vertices[19])
            vertices.append(cube.translated_vertices[11])
            vertices.append(cube.translated_vertices[21])
            
        elif (np.array_equal(cube.translated_vertices[3], cube.translated_vertices[20]) == False):
            # self.walls.append((cube.translated_vertices[20], cube.translated_vertices[3], cube.translated_vertices[2], cube.translated_vertices[19], cube.translated_vertices[11]))
            vertices.append(cube.translated_vertices[20])
            vertices.append(cube.translated_vertices[3])
            vertices.append(cube.translated_vertices[2])
            vertices.append(cube.translated_vertices[19])
            vertices.append(cube.translated_vertices[11])
            
        else:
            # self.walls.append((cube.translated_vertices[3], cube.translated_vertices[2], cube.translated_vertices[19], cube.translated_vertices[11]))
            vertices.append(cube.translated_vertices[3])
            vertices.append(cube.translated_vertices[2])
            vertices.append(cube.translated_vertices[19])
            vertices.append(cube.translated_vertices[11])

        for vertex in vertices:
            if np.isnan(vertex[0]):
                continue
            final_vertices.append(vertex)

        self.walls.append(tuple(final_vertices))

    def create_5_edge_left_wall(self, cube):

        vertices = []
        final_vertices = []
            
        if(np.array_equal(cube.translated_vertices[7], cube.translated_vertices[16]) == False):
            # self.walls.append((cube.translated_vertices[6], cube.translated_vertices[7], cube.translated_vertices[16], cube.translated_vertices[17], cube.translated_vertices[14]))  
            vertices.append(cube.translated_vertices[6])
            vertices.append(cube.translated_vertices[7])
            vertices.append(cube.translated_vertices[16])
            vertices.append(cube.translated_vertices[17])
            vertices.append(cube.translated_vertices[14])
        
        elif(np.array_equal(cube.translated_vertices[17], cube.translated_vertices[15]) == False):
            # self.walls.append((cube.translated_vertices[6], cube.translated_vertices[7], cube.translated_vertices[17], cube.translated_vertices[15], cube.translated_vertices[14]))  
            vertices.append(cube.translated_vertices[6])
            vertices.append(cube.translated_vertices[7])
            vertices.append(cube.translated_vertices[17])
            vertices.append(cube.translated_vertices[15])
            vertices.append(cube.translated_vertices[14])
        
        elif(np.array_equal(cube.translated_vertices[14], cube.translated_vertices[23]) == False):
            # self.walls.append((cube.translated_vertices[6], cube.translated_vertices[7], cube.translated_vertices[17], cube.translated_vertices[14], cube.translated_vertices[23]))  
            vertices.append(cube.translated_vertices[6])
            vertices.append(cube.translated_vertices[7])
            vertices.append(cube.translated_vertices[17])
            vertices.append(cube.translated_vertices[14])
            vertices.append(cube.translated_vertices[23])

        elif(np.array_equal(cube.translated_vertices[6], cube.translated_vertices[22]) == False):
            # self.walls.append((cube.translated_vertices[22], cube.translated_vertices[6], cube.translated_vertices[7], cube.translated_vertices[17], cube.translated_vertices[14]))  
            vertices.append(cube.translated_vertices[22])
            vertices.append(cube.translated_vertices[6])
            vertices.append(cube.translated_vertices[7])
            vertices.append(cube.translated_vertices[17])
            vertices.append(cube.translated_vertices[14])

        else:
            # self.walls.append((cube.translated_vertices[6], cube.translated_vertices[7], cube.translated_vertices[17], cube.translated_vertices[14]))  
            vertices.append(cube.translated_vertices[6])
            vertices.append(cube.translated_vertices[7])
            vertices.append(cube.translated_vertices[17])
            vertices.append(cube.translated_vertices[14])

        for vertex in vertices:
            if np.isnan(vertex[0]):
                continue
            final_vertices.append(vertex)

        self.walls.append(tuple(final_vertices))

    def create_5_edge_upper_wall(self, cube):

        vertices = []
        final_vertices = []

        if(np.array_equal(cube.translated_vertices[1], cube.translated_vertices[18]) == False):
            # self.walls.append((cube.translated_vertices[0], cube.translated_vertices[1], cube.translated_vertices[18], cube.translated_vertices[19], cube.translated_vertices[8]))
            vertices.append(cube.translated_vertices[0])
            vertices.append(cube.translated_vertices[1])
            vertices.append(cube.translated_vertices[18])
            vertices.append(cube.translated_vertices[19])
            vertices.append(cube.translated_vertices[8])

        elif(np.array_equal(cube.translated_vertices[19], cube.translated_vertices[9]) == False):
            # self.walls.append((cube.translated_vertices[0], cube.translated_vertices[1], cube.translated_vertices[19], cube.translated_vertices[9], cube.translated_vertices[8]))
            vertices.append(cube.translated_vertices[0])
            vertices.append(cube.translated_vertices[1])
            vertices.append(cube.translated_vertices[19])
            vertices.append(cube.translated_vertices[9])
            vertices.append(cube.translated_vertices[8])

        elif(np.array_equal(cube.translated_vertices[8], cube.translated_vertices[17]) == False):
            # self.walls.append((cube.translated_vertices[0], cube.translated_vertices[1], cube.translated_vertices[19], cube.translated_vertices[8], cube.translated_vertices[17]))
            vertices.append(cube.translated_vertices[0])
            vertices.append(cube.translated_vertices[1])
            vertices.append(cube.translated_vertices[19])
            vertices.append(cube.translated_vertices[8])
            vertices.append(cube.translated_vertices[17])

        elif(np.array_equal(cube.translated_vertices[0], cube.translated_vertices[16]) == False):
            # self.walls.append((cube.translated_vertices[16], cube.translated_vertices[0], cube.translated_vertices[1], cube.translated_vertices[19], cube.translated_vertices[8]))
            vertices.append(cube.translated_vertices[16])
            vertices.append(cube.translated_vertices[0])
            vertices.append(cube.translated_vertices[1])
            vertices.append(cube.translated_vertices[19])
            vertices.append(cube.translated_vertices[8])

        else:
            # self.walls.append((cube.translated_vertices[0], cube.translated_vertices[1], cube.translated_vertices[19], cube.translated_vertices[8]))
            vertices.append(cube.translated_vertices[0])
            vertices.append(cube.translated_vertices[1])
            vertices.append(cube.translated_vertices[19])
            vertices.append(cube.translated_vertices[8])

        for vertex in vertices:
            if np.isnan(vertex[0]):
                continue
            final_vertices.append(vertex)

        self.walls.append(tuple(final_vertices))

    def create_5_edge_lower_wall(self, cube):

        vertices = []
        final_vertices = []

        if(np.array_equal(cube.translated_vertices[4], cube.translated_vertices[20]) == False):
            # self.walls.append((cube.translated_vertices[5], cube.translated_vertices[4], cube.translated_vertices[20], cube.translated_vertices[21], cube.translated_vertices[13]))
            vertices.append(cube.translated_vertices[5])
            vertices.append(cube.translated_vertices[4])
            vertices.append(cube.translated_vertices[20])
            vertices.append(cube.translated_vertices[21])
            vertices.append(cube.translated_vertices[13])

        elif(np.array_equal(cube.translated_vertices[21], cube.translated_vertices[12]) == False):
            # self.walls.append((cube.translated_vertices[5], cube.translated_vertices[4], cube.translated_vertices[21], cube.translated_vertices[12], cube.translated_vertices[13]))
            vertices.append(cube.translated_vertices[5])
            vertices.append(cube.translated_vertices[4])
            vertices.append(cube.translated_vertices[21])
            vertices.append(cube.translated_vertices[12])
            vertices.append(cube.translated_vertices[13])

        elif(np.array_equal(cube.translated_vertices[13], cube.translated_vertices[23]) == False):
            # self.walls.append((cube.translated_vertices[5], cube.translated_vertices[4], cube.translated_vertices[21], cube.translated_vertices[13], cube.translated_vertices[23]))
            vertices.append(cube.translated_vertices[5])
            vertices.append(cube.translated_vertices[4])
            vertices.append(cube.translated_vertices[21])
            vertices.append(cube.translated_vertices[13])
            vertices.append(cube.translated_vertices[23])

        elif(np.array_equal(cube.translated_vertices[5], cube.translated_vertices[22]) == False):
            # self.walls.append((cube.translated_vertices[22], cube.translated_vertices[5], cube.translated_vertices[4], cube.translated_vertices[21], cube.translated_vertices[13]))
            vertices.append(cube.translated_vertices[22])
            vertices.append(cube.translated_vertices[5])
            vertices.append(cube.translated_vertices[4])
            vertices.append(cube.translated_vertices[21])
            vertices.append(cube.translated_vertices[13])

        else:
            # self.walls.append((cube.translated_vertices[5], cube.translated_vertices[4], cube.translated_vertices[21], cube.translated_vertices[13]))
            vertices.append(cube.translated_vertices[5])
            vertices.append(cube.translated_vertices[4])
            vertices.append(cube.translated_vertices[21])
            vertices.append(cube.translated_vertices[13])

        for vertex in vertices:
            if np.isnan(vertex[0]):
                continue
            final_vertices.append(vertex)

        self.walls.append(tuple(final_vertices))

    def create_and_add_walls(self, cube):

        # Front wall
        # self.walls.append((cube.translated_vertices[0], cube.translated_vertices[1], cube.translated_vertices[3], cube.translated_vertices[5]))
        
        # Back wall
        # self.walls.append((cube.translated_vertices[8], cube.translated_vertices[11], cube.translated_vertices[13]))

        # Upper wall
        # self.walls.append((cube.translated_vertices[0], cube.translated_vertices[1], cube.translated_vertices[9], cube.translated_vertices[8]))

        # # Lower wall
        # self.walls.append((cube.translated_vertices[5], cube.translated_vertices[3], cube.translated_vertices[11], cube.translated_vertices[13]))

        # Left wall
        # self.walls.append((cube.translated_vertices[5], cube.translated_vertices[0], cube.translated_vertices[8], cube.translated_vertices[13]))

        # Right wall
        # self.walls.append((cube.translated_vertices[3], cube.translated_vertices[1], cube.translated_vertices[9], cube.translated_vertices[11]))
        

        # self.create_5_edge_front_wall(cube)
        # self.create_5_edge_right_wall(cube)
        # self.create_5_edge_left_wall(cube)
        # self.create_5_edge_upper_wall(cube)
        # self.create_5_edge_lower_wall(cube)
        # self.create_5_edge_back_wall(cube)
        
        # Front wall
        vertices = [
            cube.translated_vertices[0],
            cube.translated_vertices[1],
            cube.translated_vertices[2],
            cube.translated_vertices[3],
            cube.translated_vertices[4],
            cube.translated_vertices[5],
            cube.translated_vertices[6],
            cube.translated_vertices[7],
            ]
        
        final_vertices = []

        for vertex in vertices:
            if np.isnan(vertex[0]):
                continue
            final_vertices.append(vertex)

        self.walls.append(tuple(final_vertices))

        # Right wall
        vertices = [
            cube.translated_vertices[3],
            cube.translated_vertices[2],
            cube.translated_vertices[18],
            cube.translated_vertices[19],
            cube.translated_vertices[10],
            cube.translated_vertices[11],
            cube.translated_vertices[21],
            cube.translated_vertices[20]
            ]
        
        final_vertices = []

        for vertex in vertices:
            if np.isnan(vertex[0]):
                continue
            final_vertices.append(vertex)

        self.walls.append(tuple(final_vertices))

        # Back wall
        vertices = [
            cube.translated_vertices[8],
            cube.translated_vertices[9],
            cube.translated_vertices[10],
            cube.translated_vertices[11],
            cube.translated_vertices[12],
            cube.translated_vertices[13],
            cube.translated_vertices[14],
            cube.translated_vertices[15]
            ]
        
        final_vertices = []

        for vertex in vertices:
            if np.isnan(vertex[0]):
                continue
            final_vertices.append(vertex)

        self.walls.append(tuple(final_vertices))

         # Left wall
        vertices = [
            cube.translated_vertices[16],
            cube.translated_vertices[17],
            cube.translated_vertices[15],
            cube.translated_vertices[14],
            cube.translated_vertices[23],
            cube.translated_vertices[22],
            cube.translated_vertices[6],
            cube.translated_vertices[7]
            ]
        
        final_vertices = []

        for vertex in vertices:
            if np.isnan(vertex[0]):
                continue
            final_vertices.append(vertex)

        self.walls.append(tuple(final_vertices))

        # Upper wall
        vertices = [
            cube.translated_vertices[5],
            cube.translated_vertices[4],
            cube.translated_vertices[20],
            cube.translated_vertices[21],
            cube.translated_vertices[12],
            cube.translated_vertices[13],
            cube.translated_vertices[23],
            cube.translated_vertices[22]
            ]
        
        final_vertices = []

        for vertex in vertices:
            if np.isnan(vertex[0]):
                continue
            final_vertices.append(vertex)

        self.walls.append(tuple(final_vertices))

        # Lower wall
        vertices = [
            cube.translated_vertices[0],
            cube.translated_vertices[1],
            cube.translated_vertices[18],
            cube.translated_vertices[19],
            cube.translated_vertices[9],
            cube.translated_vertices[15],
            cube.translated_vertices[17],
            cube.translated_vertices[16]
            ]
        
        final_vertices = []

        for vertex in vertices:
            if np.isnan(vertex[0]):
                continue
            final_vertices.append(vertex)

        self.walls.append(tuple(final_vertices))


    def print_intersection_points(self):
        for point in self.intersection_lines:
            print(point)

    def paint_walls(self, screen, color):
        
        for i in range(600):

            wall_id = 0
            for wall in self.walls:

                wall_points = []

                # Dla każdej krawędzi każdej ściany zbierane są współrzędne przecięcia
                for j in range(len(wall)):
                    x1, y1, _, z1 = wall[j]
                    x2, y2, _, z2 = wall[(j + 1) % len(wall)]

                    if y1 <= i <= y2 or y2 <= i <= y1:
                        if y1 == y2:
                            wall_points.append((int(x1), y1, z1, wall_id))
                            self.intersection_points.append((int(x1), y1, z1, wall_id))
                        else:
                            x = x1 + (x2 - x1) * (i - y1) / (y2 - y1)
                            z = z1 + (z2 - z1) * (i - y1) / (y2 - y1)

                            wall_points.append((int(x), i, int(z), wall_id))
                            self.intersection_points.append((int(x), i, int(z), wall_id))

                wall_id += 1
            
                if len(wall_points) == 2:
                    self.intersection_lines.append((wall_points[0], wall_points[1]))
                elif len(wall_points) == 3:

                    corner_point = None

                    if(wall_points[0][:1] == wall_points[1][:1]):
                        corner_point = wall_points[0]
                    if(wall_points[0][:1] == wall_points[2][:1]):
                        corner_point = wall_points[0]
                    if(wall_points[1][:1] == wall_points[2][:1]):
                        corner_point = wall_points[1]
                    
                    corner_lines = []

                    for k in range(len(wall)):

                        xx1, yy1, _, zz1 = wall[k]
                        xx2, yy2, _, zz2 = wall[(k + 1) % len(wall)]

                        if corner_point[:2] == (int(xx1), yy1):
                            corner_lines.append(
                                (int(xx2), yy2, zz2, wall_id)
                                )
                        if corner_point[:2] == (int(xx2), yy2):
                            corner_lines.append(
                                (int(xx1), yy1, zz1, wall_id)
                                )
                    
                    corner_point_y = corner_point[1]
                    corner_line_y_1 = corner_lines[0][1]
                    corner_line_y_2 = corner_lines[1][1]

                    if  corner_line_y_1 <= corner_point_y <= corner_line_y_2 or corner_line_y_2 <= corner_point_y <= corner_line_y_1:
                        wall_points.remove(corner_point)
                        self.intersection_points.remove(corner_point)

                    self.intersection_lines.append((wall_points[0], wall_points[1]))

                else:
                    print("Error: Wall has", len(wall_points), "points")
                        
        self.group_lines_by_y()
        self.group_intersection_points_by_y()

        self.cut_lines()

        self.paint(screen, color)

    def group_lines_by_y(self):
        
        for line in self.intersection_lines:
            y = line[0][1]
            if y not in self.intersection_lines_grouped_by_y:
                self.intersection_lines_grouped_by_y[y] = []
            self.intersection_lines_grouped_by_y[y].append(line)

    def group_intersection_points_by_y(self):

        for point in self.intersection_points:
            y = point[1]
            if y not in self.intersection_points_grouped_by_y:
                self.intersection_points_grouped_by_y[y] = []
            self.intersection_points_grouped_by_y[y].append(point)
    
    def cut_lines(self):

        index = 0

        for y_line in self.intersection_lines_grouped_by_y:
            lines = self.intersection_lines_grouped_by_y[y_line]
            lines.sort(key=lambda line: line[0][0])

            temp_lines = []

            for line in lines:

                temp_cut_points = []

                x1, y1, z1, wall_id = line[0]
                x2, y2, z2, wall_id = line[1]

                for point in self.intersection_points_grouped_by_y[y_line]:
                    
                    x, y, z, _ = point

                    if x1 < x < x2:

                        z = z1 + (z2 - z1) * (x - x1) / (x2 - x1)
                        temp_cut_points.append((x, z))
                    elif x2 < x < x1:
                        z = z1 + (z2 - z1) * (x - x1) / (x2 - x1)
                        temp_cut_points.append((x, z))

                    elif x == x1:
                        temp_cut_points.append((x, z1))
                    elif x == x2:
                        temp_cut_points.append((x, z2))
                
                temp_cut_points.sort()

                for i, cut_point_1 in enumerate(temp_cut_points):
                    for j, cut_point_2 in enumerate(temp_cut_points):
                        if cut_point_1[0] == cut_point_2[0] and i != j:
                            
                            temp_cut_points.remove(cut_point_1)
                            break

                if x1 < x2:
                    index = x1
                    zet = z1
                else:
                    index = x2
                    zet = z2

                for (cut_point, z) in temp_cut_points:

                    temp_lines.append(((index, y_line, zet, wall_id), (cut_point, y_line, z, wall_id)))
                    zet = z
                    index = cut_point

            self.cut_intersection_lines[y_line] = temp_lines
        
            index += 1

    def paint(self, screen, color):

        for y_line in self.cut_intersection_lines:
            lines = self.cut_intersection_lines[y_line]
            lines.sort(key=lambda line: self.get_max_z(line), reverse=True)

            for line in lines:
                wall_id = line[0][3]
                pygame.draw.line(screen, colors_rgb[wall_id % 24], line[0][:2], line[1][:2])

    def print_lines(self):
        for y_line in self.cut_intersection_lines:
            lines = self.cut_intersection_lines[y_line]
            lines.sort(key=lambda line: self.get_max_z(line), reverse=True)

            print("Lines for y =", y_line, ":")

            for line in lines:
                print(line)

    def get_max_z(self, line):
        return line[0][2] + line[1][2]

    def add_walls(self, cubes):
        for cube in cubes:
            self.create_and_add_walls(cube)

    def sort_walls(self):
        self.walls.sort(key=lambda wall: wall[0][2])