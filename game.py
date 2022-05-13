import pygame #agrega la libreria
import sys, os 
from spaceship import Spaceship
from constants import *
from bullet import Bullet
from enemy import Enemy

class Warship:
    def __init__(self):
        pygame.init()#inicializa el modulo
        self.width = 1000
        self.surface = pygame.display.set_mode((self.width, HEIGHT))#surface crea la ventana del juego
        self.surface_width = self.surface.get_rect().width
        self.surface_height = self.surface.get_rect().height
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('image/universe.jpg')),(self.width, HEIGHT))#agrega el background del juego
        pygame.display.set_caption(TITLE)
        self.surface.fill(BLUE)
        self.speed = 1
        self.widhtbullet = 3
        self.heightbullet = 15
        self.colorbullet = (WHITE)
        self.spaceship = Spaceship(self)
        self.bullets = pygame.sprite.Group()#permite aumentar la cantidad de balas
        self.total_bullets = 5
        self.enemies = pygame.sprite.Group()
        self._create_fleet()
    
    def run_game(self):#mantiene la ventana abierta con un loop
        while True:
            for event in pygame.event.get():#nos regresa una lista de los eventos
                if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move_right = True
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move_left = True
                    if event.key == pygame.K_SPACE:
                        self._fire_bullet()#metodo
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.spaceship.move_right = False
                    if event.key == pygame.K_LEFT:
                        self.spaceship.move_left = False

            self.spaceship.move()            
            self.surface.blit(self.background, (0, 0))
            self.spaceship.run()
            self.bullets.update()

            for bullet in self.bullets.copy():
                if bullet.rect.bottom <= 0:#vamos a borrar las balas cuando superen la ventana
                    self.bullets.remove(bullet)



            for bullet in self.bullets.sprites():
                bullet.draw_bullet()
            self.enemies.draw(self.surface)

            pygame.display.flip()

    def _fire_bullet(self):#para limitar la cantidad de balas
        if self.total_bullets != 0:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)
            self.total_bullets = self.total_bullets - 1
    
    def _create_fleet(self):
        enemy = Enemy(self)
        enemy_width = enemy.rect.width
        #self.enemies.add(enemy)
        availableSpace = self.width - (2 * enemy_width)
        numerodeEnemies = availableSpace // ( 2 * enemy_width)

        for numeroenemy in range(numerodeEnemies):
            enemy = Enemy(self)
            enemy.x = enemy_width + 2* enemy_width * numeroenemy
            enemy.rect.x = enemy.x
            self.enemies.add(enemy)

if __name__ == '__main__':
    w = Warship()
    w.run_game()


