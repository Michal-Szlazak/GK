import pygame
import sys
from model import Model


WIDTH, HEIGHT = 800, 600
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
LIGHT_BLUE = (103, 216, 200)
LIGHT_GREEN = (144, 238, 144)
LIGHT_GREY = (211, 211, 211)
DARK_GREY = (169, 169, 169)

def main():

    model = Model()

    pygame.init()
    window = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Pygame Window")

    running = True
    while running:

        event = pygame.event.wait()

        if event.type == pygame.KEYDOWN:
                
            if event.key == pygame.K_1:
                window.fill(DARK_GREY)
                print("### Computing ###")
                model.print(window, 1)
                print("### Window printed ###")

            if event.key == pygame.K_2:
                window.fill(DARK_GREY)
                print("### Computing ###")
                model.print(window, 2)
                print("### Window printed ###")

            if event.key == pygame.K_3:
                window.fill(DARK_GREY)
                print("### Computing ###")
                model.print(window, 3)
                print("### Window printed ###")

            if event.key == pygame.K_4:
                window.fill(DARK_GREY)
                print("### Computing ###")
                model.print(window, 4)
                print("### Window printed ###")

            if event.key == pygame.K_5:
                window.fill(DARK_GREY)
                print("### Computing ###")
                model.print(window, 5)
                print("### Window printed ###")

            pygame.display.flip()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    