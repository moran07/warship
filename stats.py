import pygame

class Stats:
    def __init__(self, w_game):
        self.game = w_game
        self.restart()

    def restart(self):
        self.remain_spaceships = self.game.remain_spaceships
    