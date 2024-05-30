#pgzero
# ===================================
# Proyecto Kodland Christian Iturbide
# ===================================

WIDTH, HEIGHT = 800, 500
TITLE = "Space Battle"
FPS = 60
SPEED_X = 3
SPEED_Y = 5
BULLET_SPEED = 10
MAX_BULLETS = 4
SPACESHIP1_X, SPACESHIP1_Y = 100, 100
SPACESHIP2_X, SPACESHIP2_Y = 400, 400
KEY_FIRE_PLAYER1 = keys.E
KEY_FIRE_PLAYER2 = keys.RCTRL

background = Actor("background")
spaceShip1 = Actor("spaceship1", (SPACESHIP1_X, SPACESHIP1_Y))
spaceShip2 = Actor("spaceship2", (SPACESHIP2_X, SPACESHIP2_Y))
mode = "START" # "PLAYING", "GAME_OVER"
life_player1 = 10
life_player2 = 10
bullets1 = []
bullets2 = []
winner = ""
explosion_played = False
music_playing = False

def draw():
    # Dibujar background
    background.draw()
    
    if mode == "START":
        # Dibujar mensaje de bienvenida
        msg = "Space Battle"
        screen.draw.text(msg, (80, 200), color="white", fontsize=100)
        msg = "Presione Barra espaciadora para iniciar"
        screen.draw.text(msg, (60, 400), color="white", fontsize=48)
    elif mode == "PLAYING":
        # Dibujar naves de jugadores
        spaceShip1.draw()
        spaceShip2.draw()
        
        # Dibujar score
        msg = "Player Blue: " + str(life_player1)
        screen.draw.text(msg, (40, 20), color="cyan", fontsize=40)
        msg = "Player Red: " + str(life_player2)
        screen.draw.text(msg, (440, 20), color="red", fontsize=40)
        
        # Dibujar bullets
        draw_bullets()
        
        # Dibujar planetas
        draw_planets()
        
        # Dibujar naves enemigas
        draw_enemy_spaceships()

    elif mode == "GAME_OVER":
        # Mostrar mensaje de ganador
        if winner == "player_1":
            screen.draw.text("Player 1 ha ganado!", (100, 300), color="cyan", fontsize=60)
        elif winner == "player_2":
            screen.draw.text("Player 2 ha ganado!", (100, 300), color="red", fontsize=60)
        
        mensaje = "Presione Barra espaciadora para continuar"
        screen.draw.text(mensaje, (100, 400), color="white", fontsize=40)
                     

def draw_bullets():
    for bullet in bullets1:
        bullet.draw()

    for bullet in bullets2:
        bullet.draw()    

    return

def draw_planets():
    return

def draw_enemy_spaceships():
    return
    
def update(dt):
    global music_playing, mode
    
    # Actualizar posicion de Naves, Bullets
    update_spaceship1(keyboard)
    update_spaceship2(keyboard)
    update_bullets1()
    update_bullets2()
    
    # Detectar colisiones y actualizar puntaje
    detect_collisions()
        
    # Actualizar posicion de Planetas, Enemigos
            
    return

# Checar Key event para iniciar juego
def on_key_down(key):
    global mode, KEY_FIRE_PLAYER1, KEY_FIRE_PLAYER2
    
    if mode == "START" and key == keys.SPACE:
        mode = "PLAYING"

    if mode == "PLAYING" and key == KEY_FIRE_PLAYER1:
        # Player 1 dispara
        if len(bullets1) <= MAX_BULLETS:
            bullets1.append(Actor("bullet1", (spaceShip1.x, spaceShip1.y)))
 
    if mode == "PLAYING" and key == KEY_FIRE_PLAYER2:
        # Player 2 dispara
        if len(bullets2) <= MAX_BULLETS:
            bullets2.append(Actor("bullet2", (spaceShip2.x, spaceShip2.y)))

    if mode == "GAME_OVER" and key == keys.SPACE:
        # Reinicia el juego
        mode = "START"
        restart()

    return

# spaceShip1 1 se mueve con a, s, w, d
def update_spaceship1(keyboard):
    if keyboard.w and spaceShip1.y >= 0:
        spaceShip1.y = spaceShip1.y - SPEED_Y
    elif keyboard.s and spaceShip1.y <= HEIGHT:
        spaceShip1.y = spaceShip1.y + SPEED_Y
    elif keyboard.a and spaceShip1.x >= 0:
        spaceShip1.x = spaceShip1.x - SPEED_X
    elif keyboard.d and spaceShip1.x <= WIDTH:
        spaceShip1.x = spaceShip1.x + SPEED_X
    
    return
    
# spaceShip1 2 se mueve con up, down, left, right
def update_spaceship2(keyboard):
    if keyboard.up and spaceShip2.y >= 0:
        spaceShip2.y = spaceShip2.y - SPEED_Y
    elif keyboard.down and spaceShip2.y <= HEIGHT:
        spaceShip2.y = spaceShip2.y + SPEED_Y
    elif keyboard.left and spaceShip2.x >= 0:
        spaceShip2.x = spaceShip2.x - SPEED_X
    elif keyboard.right and spaceShip2.x <= WIDTH:
        spaceShip2.x = spaceShip2.x + SPEED_X

    return

# Actualiza la posicion de los bullets de spaceship1
def update_bullets1(): 
    for i in range(len(bullets1)):    
        if bullets1[i].x > WIDTH:
            bullets1.pop(i)
            break
        else:
            bullets1[i].x = bullets1[i].x + BULLET_SPEED
            bullets1[i].angle += 2

    return

# Actualiza la posicion de los bullets de spaceship2
def update_bullets2():
    for i in range(len(bullets2)):    
        if bullets2[i].x < 0:
            bullets2.pop(i)
            break
        else:
            bullets2[i].x = bullets2[i].x - BULLET_SPEED
            bullets2[i].angle += 2

    return

def detect_collisions():
    global bullets1, spaceShip1, life_player1
    global bullets2, spaceShip2, life_player2
    global winner, mode, explosion_played
    
    # Verificar colisiones de bullets1 con spaceShip2
    for i in range(len(bullets1)):
        if bullets1[i].colliderect(spaceShip2):
            life_player2 -= 1
            bullets1.pop(i)
            break

    # Verificar colisiones de bullets2 con spaceShip1
    for i in range(len(bullets2)):
        if bullets2[i].colliderect(spaceShip1):
            life_player1 -= 1
            bullets2.pop(i)
            break
    
    # Verificar si spaceShip1 tiene 0 enegia
    if life_player1 == 0:
        # Mode es GAME_OVER y el ganador es player 2
        mode = "GAME_OVER"
        winner = "player_2"
            
    # Verificar si spaceShip2 tiene 0 enegia      
    if life_player2 == 0:
        # Mode es GAME_OVER y el ganador es player 1
        mode = "GAME_OVER"
        winner = "player_1"
        
    return


def restart():
    global life_player1, bullets1
    global life_player2, bullets2
    global mode, winner, explosion_played, music_playing
    
    #Reestablece todas las variables a su valor original
    spaceShip1.x = SPACESHIP1_X
    spaceShip1.y = SPACESHIP1_Y
    spaceShip2.x = SPACESHIP2_X
    spaceShip2.y = SPACESHIP2_Y
    mode = "START" 
    life_player1 = 10
    life_player2 = 10
    bullets1 = []
    bullets2 = []
    winner = "No winner yet"
