import pygame as py
from sys import exit
from Game_surface import Button

def main():
    py.init()
    screen = py.display.set_mode((0, 0), py.FULLSCREEN)
    py.display.set_caption("Sequence")

    clock = py.time.Clock()

    font = py.font.Font(None, 80)

    play_button = Button("PLAY", font, (0, 0, 0), (640, 360), 300, 120, (255, 255, 255))

    running = True
    while running:
        for event in py.event.get():
            if event.type == py.QUIT:
                running = False
            if event.type == py.KEYDOWN and event.key == py.K_ESCAPE:
                running = False

            if event.type == py.MOUSEBUTTONDOWN:
                if play_button.is_clicked(event.pos):
                    print("Play button clicked!")

        screen.fill((30, 30, 30))
        play_button.draw(screen)
        py.display.flip()
        clock.tick(60)

    py.quit()
    exit()

if __name__ == '__main__':
    main()