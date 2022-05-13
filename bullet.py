import pygame
from pygame.sprite import Sprite #agrupamos elementos para darles movimientos


class Bullet(Sprite):
    def __init__(self, w_game):
        super().__init__()
        self.surface = w_game.surface
        self.color = w_game.colorbullet
        self.rect = pygame.Rect(0,0, w_game.widhtbullet, w_game.heightbullet)
        self.rect.midtop = w_game.spaceship.rect.midtop
        self.game = w_game
        self.y = float(self.rect.y)#permite que bullet aumente los pixeles

    def update(self):#hace que la bala se mueva
        self.y -= self.game.speed
        self.rect.y = self.y

    def draw_bullet(self):#dibuja la bala
        pygame.draw.rect(self.surface, self.color, self.rect)