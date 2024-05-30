alien = Actor('alien')
alien.pos = 100, 56
alien.topright = 0, 10

WIDTH = 500
HEIGHT = alien.height + 20
#beep = tone.create('A3', 0.5)
beep = tone.create('E4', 0.5)
#beep = tone.create('A#5', 0.5)
#beep = tone.create('Bb3', 0.5)

    
def draw():
    screen.clear()
    alien.draw()

def update():
    alien.left += 2
    if alien.left > WIDTH:
        alien.right = 0

def on_mouse_down(pos):
    if alien.collidepoint(pos):
        set_alien_hurt()
        print("Eek!")
    else:
        print("You missed me!")
        beep.play()

def set_alien_hurt():
    alien.image = 'alien_hurt'
    sounds.eep.play()
    clock.schedule_unique(set_alien_normal, 1.0)

def set_alien_normal():
    alien.image = 'alien'