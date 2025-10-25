import pygame

pygame.init()

class Button:
    def __init__(self, text, font, color, pos):
        self.image = font.render(text, True, color).convert()
        self.rect = self.image.get_rect(center=pos)

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def is_clicked(self, mouse_pos):
        return self.rect.collidepoint(mouse_pos)