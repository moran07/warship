import pygame.font

from constants import *

class Button:
    def __init__(self, w_game, texto):
        self.surface = w_game.surface
        self.surface_rect = self.surface.get_rect()
        self.width, self.height = 500, 100
        self.color =  (YELLOW)
        self.textoColor = (BLACK)

        self.font = pygame.font.SysFont(None, 60)

        self.rect = pygame.Rect(0,0, self.width, self.height)
        self.rect.center = self.surface_rect.center

        self.prepara_texto(texto)

    def prepara_texto(self, texto):
        self.texto_image = self.font.render(texto, True, self.textoColor, self.color)
        self.texto_image_rect = self.texto_image.get_rect()
        self.texto_image_rect.center = self.rect.center

    def drawButton(self):
        self.surface.fill(self.color, self.rect)
        self.surface.blit(self.texto_image, self.texto_image_rect)