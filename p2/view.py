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
            
            if event.key == pygame.K_UP and (pygame.key.get_mods() & pygame.KMOD_SHIFT):
                model.move_y()
                window.fill(BLACK)
                model.print(window)
                pygame.display.flip()
                continue
            
            elif event.key == pygame.K_DOWN and pygame.key.get_mods() & pygame.KMOD_SHIFT:
                model.move_y_neg()
                window.fill(BLACK)
                model.print(window)
                pygame.display.flip()
                continue

            elif event.key == pygame.K_UP:
                model.move_z_neg()
                
            elif event.key == pygame.K_DOWN:
                model.move_z()
                
            elif event.key == pygame.K_LEFT:
                model.move_x()
                
            elif event.key == pygame.K_RIGHT:
                model.move_x_neg()

            elif event.key == pygame.K_w:
                model.rotate_x_neg()

            elif event.key == pygame.K_s:
                model.rotate_x()

            elif event.key == pygame.K_a:
                model.rotate_y()

            elif event.key == pygame.K_d:
                model.rotate_y_neg()

            elif event.key == pygame.K_q:
                model.rotate_z()

            elif event.key == pygame.K_e:
                model.rotate_z_neg()

            elif event.key == pygame.K_r:
                model.print(window)

            elif event.key == pygame.K_EQUALS:
                model.zoom_in()

            elif event.key == pygame.K_MINUS:
                model.zoom_out()

            elif event.key == pygame.K_p:
                model.print_vertices()
                
            elif event.key == pygame.K_LCTRL:
                model.change_paint_mode()

            elif event.key == pygame.K_v:
                model.print_intersection_points()

            elif event.key == pygame.K_r:
                model = Model()

                
            window.fill(BLACK)
            model.print(window)
            pygame.display.flip()

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
    