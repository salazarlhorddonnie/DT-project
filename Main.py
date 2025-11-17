from Game_states import States
import pygame
pygame.init()

g = States()
pygame.display.set_caption("Sequence")

while g.running:
    g.playing = True
    g.gameloop()