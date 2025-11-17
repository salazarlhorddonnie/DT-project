import pygame
from In_Game import InGame

g = InGame()

class States():
    def __init__(self):
        pygame.init()

        self.running, self.playing = True, False
        self.upKey, self.downKey, self.startKey, self.backKey = False, False, False, False

        self.DISPLAY_W, self.DISPLAY_H = 1020, 600
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        
        self.font_name = pygame.font.get_default_font()
        self.black, self.white, self.gray = (0, 0, 0), (255, 255, 255), (150, 150, 150)
        # buttons: list of dicts {id, text, rect, color}
        self.buttons = []
        # add default buttons (x, y, width, height)
        self.add_button('PLAY', 410, 250, 200, 60, id='play')
        self.add_button('OPTIONS', 410, 330, 200, 60, id='options')
        self.add_button('CREDITS', 410, 410, 200, 60, id='credits')
        self.add_button('QUIT', 410, 490, 200, 60, id='quit')

    def gameloop(self):
        while self.playing:
            self.checkevent()

            if self.startKey:
                self.playing = False

            self.display.fill(self.black)

            self.drawText('Sequence', 50, self.DISPLAY_W/2, self.DISPLAY_H/2 -100)
            self.draw_buttons()

            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.resetkeys()

    def checkevent(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running, self.playing = False, False

            if event.type == pygame.MOUSEBUTTONDOWN:
                for btn in self.buttons:
                    if btn['rect'].collidepoint(event.pos):
                        self.handle_button_click(btn['id'])
                        break

    def resetkeys(self):
        self.upKey, self.downKey, self.startKey, self.backKey = False, False, False, False

    def drawText(self, text, size, x, y):
        font = pygame.font.Font(self.font_name, size)
        textSurface = font.render(text, True, self.white)
        textRect = textSurface.get_rect(center=(x, y))
        self.display.blit(textSurface, textRect)

    # Helper: add a button definition
    def add_button(self, text, x, y, w, h, id=None, color=None):
        rect = pygame.Rect(x, y, w, h)
        self.buttons.append({
            'id': id or text.lower(),
            'text': text,
            'rect': rect,
            'color': color or self.gray
        })

    # Draw all buttons
    def draw_buttons(self):
        for btn in self.buttons:
            pygame.draw.rect(self.display, btn['color'], btn['rect'])
            self.drawText(btn['text'], 30, btn['rect'].centerx, btn['rect'].centery)

    # Map button ids to behavior
    def handle_button_click(self, btn_id):
        if btn_id == 'play':
            self.startKey = True
            g.GameUI()
        elif btn_id == 'options':
            print('Options clicked')
            # set a flag or open options menu
        elif btn_id == 'credits':
            self.show_credits()
        elif btn_id == 'quit':
            print('Quit clicked')
            self.running, self.playing = False, False

    def show_credits(self):
        credits_lines = [
            "CREDITS",
            "Lead Developer: Salazar, Lhord Donnie",
            "Developer: Tulabing, Joeross",
            "Design: Donaldo, Jan Rafael & Quirol, Renier",
            "Thanks for playing!",
            "(Click or press any key to return)"
        ]

        run = True
        while run and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    run = False
                elif event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                    run = False

            self.display.fill(self.black)
            # title + lines
            self.drawText(credits_lines[0], 48, self.DISPLAY_W/2, self.DISPLAY_H/2 - 140)
            for i, line in enumerate(credits_lines[1:], start=1):
                y = self.DISPLAY_H/2 - 80 + (i-1) * 40
                self.drawText(line, 28, self.DISPLAY_W/2, y)

            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.resetkeys()
