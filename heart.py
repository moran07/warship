import pygame
from pygame.sprite import Sprite


class Hearts(Sprite):
    def __init__(self, w_game):
        super().__init__()
        self.surface = w_game.surface
        self.surface_rect = w_game.surface.get_rect()
        self.image = pygame.image.load("image/vida.png")
        self.rect = self.image.get_rect()