from Game_states import Game

g = Game()

while g.running:
    g.playing = True
    g.gameloop()