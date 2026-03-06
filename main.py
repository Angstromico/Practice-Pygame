import pygame
from constants import WIDTH_WINDOW, HEIGHT_WINDOW

def main(): 
    pygame.init()
    window = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
