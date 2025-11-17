import pygame
pygame.init()

class InGame:
    def GameUI(self):
        
        # try reuse existing display surface if available, otherwise create one
        surface = pygame.display.get_surface()
        surface = pygame.display.set_mode((1020, 600))

        blue = (0, 0, 255)
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                    running = False

            surface.fill(blue)
            pygame.display.update()
            clock.tick(60)
