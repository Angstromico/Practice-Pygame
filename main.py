import pygame
from constants import WIDTH_WINDOW, HEIGHT_WINDOW
from character import Character

def main(): 
    pygame.init()
    window = pygame.display.set_mode((WIDTH_WINDOW, HEIGHT_WINDOW))
    pygame.display.set_caption("My First Python Game")
    run = True
    player = Character(WIDTH_WINDOW // 2, HEIGHT_WINDOW // 2)

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        player.draw(window)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()
