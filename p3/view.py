import pygame
import sys
from model import Model


WIDTH, HEIGHT = 600, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_BLUE = (103, 216, 200)
LIGHT_GREEN = (144, 238, 144)

def main():

    model = Model()

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Window")

    running = True
    while running:

        event = pygame.event.wait()

        if event.type == pygame.KEYDOWN:
                
            window.fill(BLACK)
            model.print(window)
            pygame.display.flip()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    