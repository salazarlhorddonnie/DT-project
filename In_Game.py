import pygame
pygame.init()

class InGame:
    def GameUI(self):
        
        MainSurface = pygame.display.get_surface()
        if MainSurface is None:
            MainSurface = pygame.display.set_mode((1020, 600))
        
        board_surface = pygame.image.load(r"C:\Users\Lenovo\OneDrive\Documents\GitHub\DT-project\Assets\547d5634-ea74-410e-a207-bcb962e2826a.jpg").convert_alpha()
        board = pygame.transform.scale(board_surface, (800, 570))
        disp_w, disp_h = MainSurface.get_size()
        board_rect = board.get_rect(center=(disp_w // 2, disp_h // 2))
 
        running = True
        clock = pygame.time.Clock()

        while running:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    print(event.pos)

            MainSurface.fill((137, 168, 220))
 
            MainSurface.blit(board, board_rect.topleft)
            
            pygame.display.flip()
            pygame.display.update()
            clock.tick(60)

