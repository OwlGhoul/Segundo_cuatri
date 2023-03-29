from ursina import *
import random
import math

# Definimos las constantes al principio del código
velocidad_jugador = 4
velocidad_enemigo = 2
espera_inicial = 2

app = Ursina()

window.title = "My game"
window.borderless = False
window.fullscreen = False
window.exit_button.visible = False
window.color = color.rgba(102, 51, 0, 255)

jugador = Entity(model='cube', color=color.red, collider='box')

enemigos = []

tiempo_de_inicio = None

#Agregamos una variable booleana para saber si el juego ha sido iniciado o no
juego_iniciado = False

#Movemos la creación del mensaje final al principio
mensaje_final = Text(text="¡Perdiste! El juego ha terminado.", origin=(0,0), scale=2, enabled=False)

puntos = 0
ultimo_punto = None
puntos_texto = Text(text="Puntos: " + str(puntos), origin=(-2,5), scale=2)

# Definimos la función update para globalizar todo lo que podamos 
def update():
    global enemigos, tiempo_de_inicio, juego_iniciado, mensaje_final, puntos, ultimo_punto
#Si el mensaje final está habilitado, no se actualiza el juego
    if mensaje_final.enabled:  
        return
    
    if tiempo_de_inicio is None:
        tiempo_de_inicio = time.time()
        ultimo_punto = tiempo_de_inicio 
        return

    tiempo_transcurrido = time.time() - tiempo_de_inicio
#Si el juego no ha sido iniciado, no se crean nuevos enemigos
    if not juego_iniciado:
        return

    if tiempo_transcurrido < espera_inicial:
        return
    if time.time() - ultimo_punto >= 1:
     puntos += 1
     ultimo_punto = time.time()
     puntos_texto.text = "Puntos: " + str(puntos)

    if held_keys["left arrow"]:
        jugador.x -= velocidad_jugador * time.dt
    if held_keys["right arrow"]:
        jugador.x += velocidad_jugador * time.dt
    if held_keys["up arrow"]:
        jugador.y += velocidad_jugador * time.dt
    if held_keys["down arrow"]:
        jugador.y -= velocidad_jugador * time.dt

# Creación de enemigos aleatorios
    if random.random() < 0.01:
        enemigo = Entity(model='sphere', color=color.blue, scale=(0.5,0.5,0.5), collider='sphere')
        enemigo.x = random.uniform(-5, 5)
        enemigo.y = random.uniform(-5, 5)
        enemigos.append(enemigo)

# Movimiento de los enemigos     
    for enemigo in enemigos:
        dx, dy = jugador.x - enemigo.x, jugador.y - enemigo.y
        distancia = math.sqrt(dx*dx + dy*dy)
        velocidad_x = velocidad_enemigo * dx / distancia
        velocidad_y = velocidad_enemigo * dy / distancia
        enemigo.x += velocidad_x * time.dt
        enemigo.y += velocidad_y * time.dt
        
        if jugador.intersects(enemigo).hit:
            mensaje_final = Text(text="¡Perdiste! El juego ha terminado.", origin=(0,0), scale=2)
            return
        if jugador.intersects(enemigo).hit:
            mensaje_final.enabled = True  # Habilitamos el mensaje final
            return
        
# Definimos la acción del botón de inicio     
def iniciar_juego():
    global enemigos, tiempo_de_inicio, juego_iniciado
    enemigos = []
    jugador.position = (0, 0)
    boton_inicio.visible = False

# Reiniciamos el tiempo de inicio
    tiempo_de_inicio = None

# Establecemos la variable booleana en True para indicar que el juego ha sido iniciado
    juego_iniciado = True  
boton_inicio = Button(text="Iniciar Juego", color=color.azure, scale=(0.2, 0.1), position=(0, -0.2), on_click=iniciar_juego)
boton_inicio.on_click = iniciar_juego

app.run()