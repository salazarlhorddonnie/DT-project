import pygame as py
from sys import exit

def main():
    py.init()
    screen = py.display.set_mode((0, 0), py.FULLSCREEN)
    py.display.set_caption("Sequnce")

    clock = py.time.Clock()
    running = True

    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False

        screen.fill((30, 30, 30))
        py.display.flip()
        clock.tick(60)

    py.quit()
    exit()

if __name__ == '__main__':
	main()