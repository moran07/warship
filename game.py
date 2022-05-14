import pygame #agrega la libreria
import sys, os 
from spaceship import Spaceship
from constants import *
from bullet import Bullet
from enemy import Enemy

class Warship:
    def __init__(self):
        pygame.init()#inicializa el modulo
        self.width = 800
        self.height = 500
        self.surface = pygame.display.set_mode((self.width, self.height))#surface crea la ventana del juego
        self.surface_width = self.surface.get_rect().width
        self.surface_height = self.surface.get_rect().height
        self.background = pygame.transform.scale(pygame.image.load(os.path.join('image/planet.jpg')),(self.width, self.height))#agrega el background del juego
        pygame.display.set_caption(TITLE)
        self.clock = pygame.time.Clock()
        self.surface.fill(BLUE)
        self.speed = 10
        self.widhtbullet = 3
        self.heightbullet = 15
        self.colorbullet = (WHITE)
        self.spaceship = Spaceship(self)
        self.bullets = pygame.sprite.Group()#permite aumentar la cantidad de balas
        self.total_bullets = 100
        self.enemies = pygame.sprite.Group()
        self.speed_Enemy = 4.0
        self.fleet_speed = 10
        self.fleet_direction = 1
        self.music = pygame.mixer.music.load("sound/dbz.wav")
        self.music = pygame.mixer.music.set_volume(1.0)
        self.music = pygame.mixer.music.play(-1)
        #pygame.mixer.music.set_volume(1.0) #float 0.0 - 1.0
        #pygame.mixer.music.play(-1, 0.1)
        self._create_fleet()
    
    def run_game(self):#mantiene la ventana abierta con un loop
        while True:
            self.clock.tick(FPS)
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
            self.update_Enemy()

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
        enemy_width, enemy_height = enemy.rect.size
        availableSpace = self.width - (2 * enemy_width)
        numerodeEnemies = availableSpace // ( 2 * enemy_width)
        spaceship_height = self.spaceship.rect.height
        availableSpacey = self.height - (3 * enemy_height) - spaceship_height
        numerodeFilas = availableSpacey // (2 * enemy_height)
        
        for fila in range (numerodeFilas):
            for numeroEnemy in range(numerodeEnemies):
                self.__create__enemy(numeroEnemy, fila)


    def __create__enemy(self, numeroEnemy, fila):
        enemy = Enemy(self)
        enemy_width, alien_height = enemy.rect.size
        enemy.x = enemy_width + 2* enemy_width * numeroEnemy
        enemy.rect.x = enemy.x
        enemy.rect.y = enemy.rect.height + 2*enemy.rect.height * fila
        self.enemies.add(enemy)    
                    
    def update_Enemy(self):
        self.check_bordersFleet()
        self.enemies.update()
        if not self.enemies:
            self.bullets.empty()
            self._create_fleet()
    
    def check_bordersFleet(self):
        for enemy in self.enemies.sprites():
            if enemy.check_borders():
                self.change_direction()
                break

    def change_direction(self):
        for enemy in self.enemies.sprites():
            enemy.rect.y += self.fleet_speed
        self.fleet_direction *= - 1


if __name__ == '__main__':
    w = Warship()
    w.run_game()


