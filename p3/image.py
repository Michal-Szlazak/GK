

class Image:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.pixels = [[(0, 0, 0) for _ in range(width)] for _ in range(height)]

    def print(self, window):
        for x in range(self.width):
            for y in range(self.height):
                window.set_at((x, y), self.pixels[y][x])