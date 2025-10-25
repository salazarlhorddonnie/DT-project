import pygame

pygame.init()

class Button:
    def __init__(self, text, font, text_color, pos, width=200, height=80, bg_color=(255, 255, 255)):
        self.text = text
        self.font = font
        self.text_color = text_color
        self.bg_color = bg_color

        self.rect = pygame.Rect(0, 0, width, height)
        self.rect.center = pos

        self.text_surf = font.render(text, True, text_color)
        self.text_rect = self.text_surf.get_rect(center=self.rect.center)

    def draw(self, screen):
        pygame.draw.rect(screen, self.bg_color, self.rect, border_radius=10)
        screen.blit(self.text_surf, self.text_rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)
