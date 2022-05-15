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
        self.bullets_allowed = 3
        self.enemiesScore = 50
        self.sound = pygame.mixer.Sound('sound/lazer.wav')
        self.sound.play()
        #self.sound = pygame.mixer.Sound.set_volume()

    def update(self):#hace que la bala se mueva
        self.y -= self.game.speed
        self.rect.y = self.y

        self.bullets = self.game.bullets
        self.enemies = self.game.enemies


        self.strikes = pygame.sprite.groupcollide(self.bullets, self.enemies, True, True)

        if self.strikes:
            for enemies in self.strikes.values():
                self.game.score += self.enemiesScore * len(enemies)
                self.game.scoreP.prep_score()
                self.game.scoreP.check_HighScore()

    def draw_bullet(self):#dibuja la bala
        pygame.draw.rect(self.surface, self.color, self.rect)