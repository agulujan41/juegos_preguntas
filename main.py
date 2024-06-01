from questions import preguntas,respuestas_correctas,respuestas_incorrectas1,respuestas_incorrectas2,respuestas_incorrectas3
from random import * 
from time import *
from test import analizador
respuestas0 = [respuestas_correctas[0],respuestas_incorrectas1[0],respuestas_incorrectas2[0],respuestas_incorrectas3[0]]
shuffle(respuestas0)
respuestas1 = [respuestas_correctas[1],respuestas_incorrectas1[1],respuestas_incorrectas2[1],respuestas_incorrectas3[1]]
shuffle(respuestas1)
respuestas2 = [respuestas_correctas[2],respuestas_incorrectas1[2],respuestas_incorrectas2[2],respuestas_incorrectas3[2]]
shuffle(respuestas2)
respuestas3 = [respuestas_correctas[3],respuestas_incorrectas1[3],respuestas_incorrectas2[3],respuestas_incorrectas3[3]]
shuffle(respuestas3)
respuestas4 = [respuestas_correctas[4],respuestas_incorrectas1[4],respuestas_incorrectas2[4],respuestas_incorrectas3[4]]
shuffle(respuestas4)

print("Hola , Bienvenidos a la trivia de la Copa America")
input ("Estas listo: ")

print("Empezamos...")
sleep(3)
print("Primera pregunta:")
print(preguntas[0])
for i in range(len(respuestas0)):
    print(i+1,"-",respuestas0[i])
respuesta_usuario = int(input("Ingresar respuesta con un numero: "))
respuesta_usuario = respuesta_usuario-1
print(analizador(0,respuestas0[respuesta_usuario]))
print("Segunda pregunta:")
print(preguntas[1])
for i in range(len(respuestas1)):
    print(i+1,"-",respuestas1[i])
respuesta_usuario = int(input("Ingresar respuesta con un numero: "))
respuesta_usuario = respuesta_usuario-1
print(analizador(1,respuestas1[respuesta_usuario]))
print("Tercera pregunta:")
print(preguntas[2])
for i in range(len(respuestas2)):
    print(i+1,"-",respuestas2[i])
respuesta_usuario = int(input("Ingresar respuesta con un numero: "))
respuesta_usuario = respuesta_usuario-1
print(analizador(2,respuestas2[respuesta_usuario]))
print("Cuarta pregunta:")
print(preguntas[3])
for i in range(len(respuestas3)):
    print(i+1,"-",respuestas3[i])
respuesta_usuario = int(input("Ingresar respuesta con un numero: "))
respuesta_usuario = respuesta_usuario-1
print(analizador(3,respuestas3[respuesta_usuario]))
print("Quinta pregunta:")
print(preguntas[4])
for i in range(len(respuestas4)):
    print(i+1,"-",respuestas4[i])
respuesta_usuario = int(input("Ingresar respuesta con un numero: "))
respuesta_usuario = respuesta_usuario-1
print(analizador(4,respuestas4[respuesta_usuario]))
print("Gracias por jugar")
print("Hasta la proxima")