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
    font = pygame.font.Font(None, 14)

    clock = pygame.time.Clock()

    running = True
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        keys_pressed = pygame.key.get_pressed()

        if keys_pressed[pygame.K_LSHIFT] and keys_pressed[pygame.K_UP]:
            model.move_y()

        elif keys_pressed[pygame.K_LSHIFT] and keys_pressed[pygame.K_DOWN]:
            model.move_y_neg()
        
        elif keys_pressed[pygame.K_UP]:
            model.move_z_neg()
            
        elif keys_pressed[pygame.K_DOWN]:
            model.move_z()
            
        elif keys_pressed[pygame.K_LEFT]:
            model.move_x()
            
        elif keys_pressed[pygame.K_RIGHT]:
            model.move_x_neg()

        elif keys_pressed[pygame.K_w]:
            model.rotate_x_neg()

        elif keys_pressed[pygame.K_s]:
            model.rotate_x()

        elif keys_pressed[pygame.K_a]:
            model.rotate_y()

        elif keys_pressed[pygame.K_d]:
            model.rotate_y_neg()

        elif keys_pressed[pygame.K_q]:
            model.rotate_z()

        elif keys_pressed[pygame.K_e]:
            model.rotate_z_neg()

        elif keys_pressed[pygame.K_r]:
            model.print(window)

        elif keys_pressed[pygame.K_EQUALS]:
            model.zoom_in()

        elif keys_pressed[pygame.K_MINUS]:
            model.zoom_out()

        elif keys_pressed[pygame.K_p]:
            model.print_vertices()

        elif keys_pressed[pygame.K_r]:
            model = Model()
                    
        clock.tick(60) # 60 FPS
        window.fill(BLACK)
        model.print(window)


        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    