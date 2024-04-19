from cube import Cube
import math
import pygame

WHITE = (255, 255, 255)
GREY = (128, 128, 128)

colors_rgb = [
    (255, 102, 102),   # Light Red
    (255, 178, 102),   # Light Orange
    (255, 255, 102),   # Light Yellow
    (178, 255, 102),   # Light Green
    (102, 255, 255),   # Light Cyan
    (102, 178, 255),   # Light Blue
    (178, 102, 255),   # Light Purple
    (255, 153, 204),   # Light Pink
    (255, 204, 204),   # Light Peach
    (255, 204, 102),   # Light Gold
    (204, 255, 102),   # Light Lime
    (153, 204, 255)    # Light Sky Blue
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

    def create_and_add_walls(self, cube):
        # self.walls = []

        # # Front wall
        self.walls.append((cube.translated_vertices[0], cube.translated_vertices[1], cube.translated_vertices[3], cube.translated_vertices[5]))

        # # Back wall
        self.walls.append((cube.translated_vertices[8], cube.translated_vertices[9], cube.translated_vertices[11], cube.translated_vertices[13]))

        # # Upper wall
        cube.walls.append((cube.translated_vertices[0][:2], cube.translated_vertices[1][:2], cube.translated_vertices[8][:2], cube.translated_vertices[9][:2]))

        # # # Lower wall
        self.walls.append((cube.translated_vertices[5], cube.translated_vertices[3], cube.translated_vertices[11], cube.translated_vertices[13]))

        # # Left wall
        self.walls.append((cube.translated_vertices[5], cube.translated_vertices[0], cube.translated_vertices[8], cube.translated_vertices[13]))

        # # Right wall
        self.walls.append((cube.translated_vertices[3], cube.translated_vertices[1], cube.translated_vertices[9], cube.translated_vertices[11]))


    def print_intersection_points(self):
        for point in self.intersection_lines:
            print(point)

    def paint_walls(self, cube, screen, color):
        
        for i in range(600):

            wall_id = 0
            for wall in self.walls:

                wall_points = []

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
                            # distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
                            # z = distance
                            wall_points.append((int(x), i, int(z), wall_id))
                            self.intersection_points.append((int(x), i, int(z), wall_id))

                wall_id += 1
            
                if len(wall_points) == 2:
                    self.intersection_lines.append((wall_points[0], wall_points[1]))
                elif len(wall_points) == 3:

                    corner_point = None
                    # print("Wall points", wall_points)

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

                        # print("Corner point", corner_point, "Line", (int(xx1), yy1, zz1, wall_id), (int(xx2), yy2, zz2, wall_id))

                        if corner_point[:2] == (int(xx1), yy1):
                            # print("Found Corner point", corner_point,(int(xx2), yy2, zz2, wall_id))
                            corner_lines.append(
                                (int(xx2), yy2, zz2, wall_id)
                                )
                        if corner_point[:2] == (int(xx2), yy2):
                            # print("Found Corner point", corner_point, (int(xx1), yy1, zz1, wall_id))
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

                elif len(wall_points) == 4:
                    print("Error: Wall points are 4")
                        
                            




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

        max_y = max(self.intersection_lines_grouped_by_y.keys())
        min_y = min(self.intersection_lines_grouped_by_y.keys())

        # index = min_y
        # for y_line in range(min_y, max_y + 1):  # Iterate over all y-coordinates from min_y to max_y
        #     if y_line not in self.intersection_lines_grouped_by_y:  # Check if the y-coordinate is missing
        #         print("Missing line after grouping at y =", y_line)

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

                # print("Cut points", temp_cut_points)

                for i, cut_point_1 in enumerate(temp_cut_points):
                    for j, cut_point_2 in enumerate(temp_cut_points):
                        if cut_point_1[0] == cut_point_2[0] and i != j:
                            
                            temp_cut_points.remove(cut_point_1)
                            # temp_cut_points.remove(cut_point_2)
                            break

                index = x1
                zet = z1

                for (cut_point, z) in temp_cut_points:

                    temp_lines.append(((index, y_line, zet, wall_id), (cut_point, y_line, z, wall_id)))
                    zet = z
                    index = cut_point

                temp_lines.append(((index, y_line, zet, wall_id), (x2, y_line, z2, wall_id)))

            self.cut_intersection_lines[y_line] = temp_lines
        
            index += 1

    def paint(self, screen, color):

        for y_line in self.cut_intersection_lines:
            lines = self.cut_intersection_lines[y_line]
            lines.sort(key=lambda line: self.get_max_z(line), reverse=True)

            # print("Lines for y =", y_line, ":")

            for line in lines:
                wall_id = line[0][3]
                pygame.draw.line(screen, colors_rgb[wall_id % 12], line[0][:2], line[1][:2])
                # print(line)

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


