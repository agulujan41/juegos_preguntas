import pygame
import textArea
pygame.init()
ANCHO = 500
ALTO = 500
DIMENSION = (ANCHO,ALTO)
pantalla = pygame.display.set_mode(DIMENSION)
pygame.display.set_caption("Trivia")
#COLORES
ROJO = (255,0,0)
VERDE = (0,255,0)
AZUL = (0,0,255)
NEGRO = (0,0,0)
BLANCO = (255,255,255)

presentacion_juego = textArea.TextArea(0,0,500,100,pantalla,BLANCO)
presentacion_juego.cambiarTexto("Bienvenidos al juego",70,NEGRO)
continuar = textArea.TextArea(0,200,500,100,pantalla,BLANCO)
continuar.cambiarTexto("Presione espacio para continuar...",35,NEGRO)

cartel_pregunta = textArea.TextArea(0,0,500,100,pantalla,ROJO)
cartel_pregunta.cambiarTexto("Pregunta ...",35,BLANCO)

def pregunta0():
    while True:
        pantalla.fill(ROJO)
        cartel_pregunta.dibujar(0,0)
        cartel_pregunta.cambiarTexto("Pregunta n° 1",35,BLANCO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pregunta1()
    
        pygame.display.update()

def pregunta1():
     while True:
        pantalla.fill(ROJO)
        cartel_pregunta.dibujar(0,0)
        cartel_pregunta.cambiarTexto("Pregunta n° 2",35,BLANCO)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pregunta2()
    
        pygame.display.update()

def pregunta2():
    pass
while True:
    pantalla.fill(BLANCO)
    presentacion_juego.dibujar(0,0)
    continuar.dibujar(0,0)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                pregunta0()
    
    pygame.display.update()