import pygame

class menu():
    def __init__(self, game):
        self.game = game 
        self.midW, self.midH = self.game.DISPLAY_W/2, self.game.DISPLAY_H/2
        self.runDisplay = True

    def blitScreen(self):
        self.game.window.blit(self.game.display, (0,0))
            pygame.display.update()
            self.game.resetkeys()

class MainMenu(menu):
    