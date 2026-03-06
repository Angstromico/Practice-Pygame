import pygame
from constants import WIDTH_CHARACTER, HEIGHT_CHARACTER, COLOR_CHARACTER

class Character:
    def __init__(self, x, y):
        self.shape = pygame.Rect(0, 0, WIDTH_CHARACTER, HEIGHT_CHARACTER)
        self.shape.center = (x, y)

    def draw(self, window):
        pygame.draw.rect(window, COLOR_CHARACTER, self.shape)
