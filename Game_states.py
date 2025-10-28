import pygame

class Game():
    def __init__(self):
        pygame.init()

        self.running, self.playing = True, False
        self.upKey, self.downKey, self.startKey, self.backKey = False, False, False, False
        self.DISPLAY_W, self.DISPLAY_H = 1020, 600
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        self.font_name = pygame.font.get_default_font()
        self.black, self.white, self.gray = (0, 0, 0), (255, 255, 255), (150, 150, 150)

        # Create a button (x, y, width, height)
        self.button_rect = pygame.Rect(410, 350, 200, 60)

    def gameloop(self):
        while self.playing:
            self.checkevent()

            if self.startKey:
                self.playing = False

            self.display.fill(self.black)

            # Draw title and button
            self.drawText('Sequence', 50, self.DISPLAY_W/2, self.DISPLAY_H/2 - 100)
            pygame.draw.rect(self.display, self.gray, self.button_rect)
            self.drawText('PLAY', 30, self.button_rect.centerx, self.button_rect.centery)

            # Show display
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.resetkeys()

    def checkevent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.button_rect.collidepoint(event.pos):
                    print("Button clicked!")
                    self.startKey = True  # Example: make it stop the loop or start game

    def resetkeys(self):
        self.upKey, self.downKey, self.startKey, self.backKey = False, False, False, False

    def drawText(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        textSurface = font.render(text, True, self.white)
        textRect = textSurface.get_rect(center=(x, y))
        self.display.blit(textSurface, textRect)
