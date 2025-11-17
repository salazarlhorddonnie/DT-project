import pygame
from In_Game import InGame
import os  # <-- add import for os module

g = InGame()

class States():
    def __init__(self):
        pygame.init()

        self.running, self.playing = True, False
        self.upKey, self.downKey, self.startKey, self.backKey = False, False, False, False

        self.DISPLAY_W, self.DISPLAY_H = 1020, 600
        self.display = pygame.Surface((self.DISPLAY_W, self.DISPLAY_H))
        self.window = pygame.display.set_mode((self.DISPLAY_W, self.DISPLAY_H))
        
        self.font_path = r"C:\Users\Lenovo\OneDrive\Documents\GitHub\DT-project\Assets\PixelifySans-VariableFont_wght.ttf"
        self.sys_font = None
        
        self._font_cache = {}
        self.black, self.white, self.gray = (0, 0, 0), (255, 255, 255), (150, 150, 150)

        self.buttons = []
        
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

    def get_font(self, size):
        if size in self._font_cache:
            return self._font_cache[size]
        try:
            if self.font_path and os.path.isfile(self.font_path):
                f = pygame.font.Font(self.font_path, size)
            elif self.sys_font:
                f = pygame.font.SysFont(self.sys_font, size)
            else:
                f = pygame.font.Font(None, size)
        except Exception:
            f = pygame.font.Font(None, size)
        self._font_cache[size] = f
        return f

    def drawText(self, text, size, x, y):
        font = self.get_font(size)
        textSurface = font.render(text, True, self.white)
        textRect = textSurface.get_rect(center=(x, y))
        self.display.blit(textSurface, textRect)

    def add_button(self, text, x, y, w, h, id=None, color=None):
        rect = pygame.Rect(x, y, w, h)
        self.buttons.append({
            'id': id or text.lower(),
            'text': text,
            'rect': rect,
            'color': color or self.gray
        })

    def draw_buttons(self):
        for btn in self.buttons:
            pygame.draw.rect(self.display, btn['color'], btn['rect'])
            self.drawText(btn['text'], 30, btn['rect'].centerx, btn['rect'].centery)

    def handle_button_click(self, btn_id):
        if btn_id == 'play':
            self.startKey = True
            g.GameUI()
        elif btn_id == 'options':
            self.show_options()
        elif btn_id == 'credits':
            self.show_credits()
        elif btn_id == 'quit':
            self.running, self.playing = False, False

    def show_credits(self):
        credits_lines = [
            "CREDITS",
            "Lead Developer: Salazar, Lhord Donnie",
            "Developer: Tulabing, Joeross",
            "Design: Donaldo, Jan Rafael & Quirol, Renier",
            "Thanks for playing!",
        ]

        run = True
        while run and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False

            self.display.fill(self.black)
            self.drawText(credits_lines[0], 48, self.DISPLAY_W/2, self.DISPLAY_H/2 - 140)
            for i, line in enumerate(credits_lines[1:], start=1):
                y = self.DISPLAY_H/2 - 80 + (i-1) * 40
                self.drawText(line, 28, self.DISPLAY_W/2, y)

            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.resetkeys()

    def show_options(self):
        btn_w, btn_h = 300, 60
        x = (self.DISPLAY_W - btn_w) // 2
        y_full = self.DISPLAY_H // 2 - 60
        y_win = y_full + 90

        fullscreen_rect = pygame.Rect(x, y_full, btn_w, btn_h)
        windowed_rect = pygame.Rect(x, y_win, btn_w, btn_h)
 
        run = True
        while run and self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    run = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        run = False
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if fullscreen_rect.collidepoint(event.pos):
                        self.window = pygame.display.set_mode(
                            (self.DISPLAY_W, self.DISPLAY_H), pygame.FULLSCREEN
                        )
                    elif windowed_rect.collidepoint(event.pos):
                        self.window = pygame.display.set_mode(
                            (self.DISPLAY_W, self.DISPLAY_H)
                        )
 
            self.display.fill(self.black)
            self.drawText("OPTIONS", 48, self.DISPLAY_W/2, self.DISPLAY_H/2 - 160)
 
            pygame.draw.rect(self.display, self.gray, fullscreen_rect)
            pygame.draw.rect(self.display, self.gray, windowed_rect)
 
            self.drawText("Fullscreen", 30, fullscreen_rect.centerx, fullscreen_rect.centery)
            self.drawText("Windowed", 30, windowed_rect.centerx, windowed_rect.centery)
            font = pygame.font.Font(self.font_path, 24)
            label = font.render("Bugged", True, self.white)
            label_rect = label.get_rect(midleft=(fullscreen_rect.right + 10, fullscreen_rect.centery))
            self.display.blit(label, label_rect)
 
            self.window.blit(self.display, (0, 0))
            pygame.display.update()
            self.resetkeys()
