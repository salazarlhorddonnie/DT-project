import pygame
pygame.init()

class InGame:
    def GameUI(self):

        MainSurface = pygame.display.set_mode((1020, 600))
        BoardSurface = pygame.Surface((510, 300))

        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False

            MainSurface.fill((128, 128, 128))   
            BoardSurface.fill((255, 255, 255)) 

            MainSurface.blit(BoardSurface, (255, 150))

            pygame.display.update()
            clock.tick(60)
