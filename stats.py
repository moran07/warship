import pygame

class Stats:
    def __init__(self, w_game):
        self.restart()
        self.game = w_game

    def restart(self):
        self.remain_spaceships = self.game.remain_spaceships
    