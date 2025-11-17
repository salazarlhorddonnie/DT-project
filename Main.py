from Game_states import States

g = States()

while g.running:
    g.playing = True
    g.gameloop()