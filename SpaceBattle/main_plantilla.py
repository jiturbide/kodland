#pgzero
# ===================================
# Proyecto Kodland Christian Iturbide
# ===================================

WIDTH, HEIGHT = 800, 500
TITLE = "Space Battle"
FPS = 60
SPEED_X = 3
SPEED_Y = 5
BULLET_SPEED = 7
MAX_BULLETS = 3
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
winner = "No winner yet"

def draw():
    # Dibujar background
    
    if mode == "START":
        # Dibujar mensaje de bienvenida
        msg = "Space Battle"
        screen.draw.text(msg, (80, 200), color="white", fontsize=100)
        msg = "Presione Barra espaciadora para iniciar"
        screen.draw.text(msg, (60, 400), color="white", fontsize=48)
    elif mode == "PLAYING":
        # Dibujar naves de jugadores
        
        # Dibujar score
        #msg = "Player Blue: " + str(life_player1)
        #screen.draw.text(msg, (40, 20), color="cyan", fontsize=40)

        #msg = "Player Red: " + str(life_player2)
        
        # Dibujar bullets
        draw_bullets()
        
        # Dibujar planetas
        draw_planets()
        
        # Dibujar naves enemigas
        draw_enemy_spaceships()

    elif mode == "GAME_OVER":
        # Mostrar mensaje de ganador
        '''
        if winner == "player_1":
            screen.draw.text("Player 1 ha ganado!", (100, 300), color="cyan", fontsize=60)
        elif winner == "player_2":
            screen.draw.text("Player 2 ha ganado!", (100, 300), color="red", fontsize=60)
        
        mensaje = "Presione Barra espaciadora para continuar"
        screen.draw.text(mensaje, (100, 400), color="white", fontsize=40)
        ''' 
    return

def draw_bullets():
    pass

def draw_planets():
    pass

def draw_enemy_spaceships():
    pass
    
def update(dt):
    global music_playing, mode
    
    # Actualizar posicion de Naves, Bullets
    
    # Detectar colisiones y actualizar puntaje

    # Iniciar la reproduccion de la musica
        
    # Actualizar posicion de Planetas, Enemigos
            

# Checar Key event para iniciar juego
def on_key_down(key):
    global mode, SPEED
    
    if mode == "START" and key == keys.SPACE:
        mode = "PLAYING"

    if mode == "PLAYING" and key == KEY_FIRE_PLAYER1:
        # Player 1 dispara
        pass
    
    if mode == "PLAYING" and key == KEY_FIRE_PLAYER2:
        # Player 2 dispara
        pass
    
    if mode == "GAME_OVER" and key == keys.SPACE:
        mode = "START"
        
        restart()


# spaceShip1 1 se mueve con a, s, w, d
def update_spaceship1(keyboard):

    return
    
# spaceShip1 2 se mueve con up, down, left, right
def update_spaceship2(keyboard):

    return

# Actualiza la posicion de los bullets de spaceship1
def update_bullets1(): 
    
    return

# Actualiza la posicion de los bullets de spaceship2
def update_bullets2():

    return

def detect_collisions():
    global bullets1, spaceShip1, life_player1
    global bullets2, spaceShip2, life_player2
    global winner, mode
    
    # Verificar colisiones de bullets1 con spaceShip2
    '''
    for i in range(len(bullets1)):
        if bullets1[i].colliderect(spaceShip2):
            life_player2 -= 1
            bullets1.pop(i)
            break
    '''
    # Verificar colisiones de bullets2 con spaceShip1

    
    # Verificar si spaceShip1 tiene 0 enegia
    '''
    if life_player1 == 0:
        # Mode es GAME_OVER y el ganador es player 2
        mode = "GAME_OVER"
        winner = "player_2"
    '''
    # Verificar si spaceShip2 tiene 0 enegia  
    # Mode es GAME_OVER y el ganador es player 1

    return
    
    
def restart():
    global life_player1, bullets1
    global life_player2, bullets2
    global mode, winner
    
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
