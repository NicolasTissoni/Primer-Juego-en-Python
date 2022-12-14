import pygame, sys
import time
from pygame.locals import *

# Importar clases
from clases import jugador
from clases import asteroide
from random import randint

# Variables
ANCHO = 448
ALTO = 640
listaAsteroides = []
puntos = 0
colorFuente = (120, 200, 40)

# booleano juego
jugando = True

# Function Principal

# Cargar asteroides
def cargarAsteroides(x, y):
    meteoro = asteroide.Asteroide(x, y)
    listaAsteroides.append(meteoro)
    
def gameOver():
    global jugando
    jugando = False
    for meteoritos in listaAsteroides:
        listaAsteroides.remove(meteoritos)

def meteoritos():
    pygame.init()
    ventana = pygame.display.set_mode((ANCHO, ALTO))
    
    # Imagen de Fondo
    fondo = pygame.image.load("imagenes/fondo-espacio.jpg")
    
    # Titulo
    pygame.display.set_caption("Meteoritos")
    
    # crea objeto jugador
    nave = jugador.Nave()
    contador = 0
    
    # Sonidos
    sonido_fondo = pygame.mixer.Sound("sonidos/fondo.wav")
    sonido_fondo.play()
    sonido_fondo.set_volume(0.3)
    
    # Fuente Marcador
    fuenteMarcador = pygame.font.SysFont("Arial", 50)
    
    sonido_colision = pygame.mixer.Sound("sonidos/colision.wav")
    pygame.mixer.Sound.play(sonido_colision)
    
    # Ciclo de Juego
    while True:
        ventana.blit(fondo, (0, 0))
        nave.dibujar(ventana)

        # Tiempo
        tiempo = time.time()
        
        # Marcador
        global puntos
        textoMarcador = fuenteMarcador.render("Puntos: "+str(puntos), 0, colorFuente)
        ventana.blit(textoMarcador, (0, 0))
        
        # Crea asteroides
        if nave.vida == True:
            if tiempo - contador > 1:
                contador = tiempo
                posX = randint(2, 400)
                cargarAsteroides(posX, 0)

        # Comprobar listaAsteroides
        if len(listaAsteroides) > 0:
            for x in listaAsteroides:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.top > 640:
                    listaAsteroides.remove(x)
                else:
                    if x.rect.colliderect(nave.rect):
                        listaAsteroides.remove(x)
                        sonido_colision.play()
                        nave.vida = False
                        gameOver()

        # Disparo de proyectil
        if len(nave.listaDisparo) > 0:
            for x in nave.listaDisparo:
                x.dibujar(ventana)
                x.recorrido()
                if x.rect.top < -10:
                    nave.listaDisparo.remove(x)
                else:
                    for meteoritos in listaAsteroides:
                        if x.rect.colliderect(meteoritos):
                            listaAsteroides.remove(meteoritos)
                            nave.listaDisparo.remove(x)
                            puntos += 1
        nave.mover()

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if jugando == True:
                    if event.key == K_LEFT:
                        nave.rect.left -= nave.velocidad
                    elif event.key == K_RIGHT:
                        nave.rect.right += nave.velocidad
                    elif event.key == K_SPACE:
                        x, y = nave.rect.center
                        nave.disparar(x, y)
        if jugando == False:
            fuenteGameOver = pygame.font.SysFont("Arial", 50)
            textoGameOver = fuenteGameOver.render("Game Over", 0, colorFuente)
            ventana.blit(textoGameOver, (120, 250))
            pygame.mixer.music.fadeout(3000)
        
        pygame.display.update()

# Llamada a funcion principal
meteoritos()