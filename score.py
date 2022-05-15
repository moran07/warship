import pygame.font

from constants import WHITE

class Score:
    def __init__(self, w_game):
        self.surface = w_game.surface
        self.surface_rect = self.surface.get_rect()
        self.game = w_game
        self.stats = w_game.stats

        self.textColor = (WHITE)
        self.font = pygame.font.SysFont(None, 48)
        self.prep_score()
        self.prep_HighScore()

    def prep_score(self):
        self.scoreStr = str(self.game.score)
        self.scoreImage = self.font.render(self.scoreStr, True, self.textColor, None)

        self.score_rect = self.scoreImage.get_rect()
        self.score_rect.right = self.surface_rect.right - 20
        self.score_rect.top = 20
    
    def prep_HighScore(self):
        self.HighScoreStr = str(self.game.HighScore)
        self.HighscoreImage = self.font.render(self.HighScoreStr, True, self.textColor, None)

        self.HighScore_rect = self.HighscoreImage.get_rect()
        self.HighScore_rect.centerx = self.surface_rect.centerx
        self.HighScore_rect.top = self.surface_rect.top

    def check_HighScore(self):   
        if self.game.score > self.game.HighScore:
            self.game.HighScore = self.game.score
            self.prep_HighScore()

    def showScore(self):
        self.surface.blit(self.scoreImage, self.score_rect)
        self.surface.blit(self.HighscoreImage, self.HighScore_rect)
