import pygame

def main(): 
    pygame.init()
    width, height = 800, 600
    window = pygame.display.set_mode((width, height))
    run = True

    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    pygame.quit()

if __name__ == "__main__":
    main()
