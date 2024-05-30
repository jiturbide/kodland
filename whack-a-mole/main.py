# WHACK A MOLE GAME
WIDTH = 1024
HEIGHT = 768
background = Actor("background_initial")
mole = Actor("mole_gray")
mallet = Actor("mallet_up")
mode = "INITIAL"
    
def draw():
    screen.clear()
    background.draw()
    
    if mode == "PLAYING":
        mole.draw()
        mallet.draw()

def update(dt):
    global mode
    if mode == "INITIAL" and keyboard.SPACE:
        mode = "PLAYING"
        background.image = "background_playing"

def on_mouse_down(button, pos):
    if button == mouse.LEFT:
        set_mallet_down()

def on_mouse_move(pos):
    mallet.pos = pos
    
def set_mallet_down():
    mallet.image = "mallet_down"
    sounds.eep.play()
    clock.schedule_unique(set_mallet_up, 0.1)
    
def set_mallet_up():
    mallet.image = "mallet_up"
