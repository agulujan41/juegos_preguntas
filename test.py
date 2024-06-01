from question import preguntas,respuestas_correctas
def analizador(posicionPregunta,respuestaUsuario):
    if posicionPregunta == 0 :
        if respuestaUsuario == respuestas_correctas[0]:
            return True
        else:
            return False
    elif posicionPregunta == 1 :
        if respuestaUsuario == respuestas_correctas[1]:
            return True
        else:
            return False
    elif posicionPregunta == 2 :
        if respuestaUsuario == respuestas_correctas[2]:
            return True
        else:
            return False
    elif posicionPregunta == 3 :
        if respuestaUsuario == respuestas_correctas[3]:
            return True
        else:
            return False
    elif posicionPregunta == 4 :
        if respuestaUsuario == respuestas_correctas[4]:
            return True
        else:
            return False