import pygame
from pygame.sprite import Sprite


class Enemy(Sprite):
    def __init__(self, w_game, ):
        super().__init__()
        self.surface = w_game.surface

        self.image = pygame.image.load("image/nave.pro.png")
        self.rect = self.image.get_rect()


        #self.rect.midtop = (WIDTH // 2, 50)#ubicar al enemy en la parte superior del surface
        #self.rect.midtop = (HEIGHT // 2, 50)

        self.rect.x = self.rect.width #dejar un espacio que sea igual al ancho y al alto del enemy
        self.rect.y = self.rect.height


        self.x = float(self.rect.x)#es para tener registro de la posicion orizontal
        self.game = w_game
        #self.speed_Enemy = w_game.speed_Enemy

    def update(self):
        self.x += (self.game.speed_Enemy * self.game.fleet_direction) #ubicamos la posicion de enemy
        self.rect.x = self.x #damos movimiento al enemy

    def check_borders(self):
        surface_rect = self.surface.get_rect()
        if self.rect.right >= surface_rect.right or self.rect.left <= 0:
            return True
        self.bullets = self.game.bullets
        self.enemies = self.game.enemies
        strikes = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)
