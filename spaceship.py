import pygame

#aqui creo al personaje principal
class Spaceship:
    def __init__(self, w_game):
        self.surface = w_game.surface
        self.surface_rect = w_game.surface.get_rect()#nos permite poner la nave y crea un rectangulo
        self.image = pygame.image.load("image/bardock.png")
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.surface_rect.midbottom
        self.move_right = False
        self.move_left = False

    def move(self):
        if self.move_right and self.rect.right < self.surface_rect.right:
            self.rect.x += 5
        if self.move_left and self.rect.left > 0:
            self.rect.x -= 5
    
    def run(self):
        self.surface.blit(self.image, self.rect)

    def center_spaceship(self):
        self.rect.midbottom = self.surface_rect.midbottom
        self.x = float(self.rect.x)