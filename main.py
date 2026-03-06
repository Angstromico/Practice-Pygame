import pygame
from constants import width, height

def main(): 
    pygame.init()
    window = pygame.display.set_mode((width, height))
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
