Juego de Memoria

Autor: Julio Cesar Perez Rodriguez
Matricula: A01705763

Actividades:
 1. Solucionar Errores Flake8
 2. Contar y desplegar el numero de taps
 3.Detectar cuando todos los cuadros se han destapado

Errores al inicio del codigo:

C:\Users\julio\OneDrive\Desktop\Escuela\TC1001S\Proyecto_Equipo4\Juego_Memoria>python -m flake8 memory.py
memory.py:12:1: F403 'from random import *' used; unable to detect undefined names
memory.py:13:1: F403 'from turtle import *' used; unable to detect undefined names
memory.py:25:5: F405 'up' may be undefined, or defined from star imports: random, turtle
memory.py:26:5: F405 'goto' may be undefined, or defined from star imports: random, turtle
memory.py:27:5: F405 'down' may be undefined, or defined from star imports: random, turtle
memory.py:28:5: F405 'color' may be undefined, or defined from star imports: random, turtle
memory.py:29:5: F405 'begin_fill' may be undefined, or defined from star imports: random, turtle
memory.py:31:9: F405 'forward' may be undefined, or defined from star imports: random, turtle
memory.py:32:9: F405 'left' may be undefined, or defined from star imports: random, turtle
memory.py:33:5: F405 'end_fill' may be undefined, or defined from star imports: random, turtle
memory.py:61:5: F405 'clear' may be undefined, or defined from star imports: random, turtle
memory.py:62:5: F405 'goto' may be undefined, or defined from star imports: random, turtle
memory.py:63:5: F405 'shape' may be undefined, or defined from star imports: random, turtle
memory.py:64:5: F405 'stamp' may be undefined, or defined from star imports: random, turtle
memory.py:75:9: F405 'up' may be undefined, or defined from star imports: random, turtle
memory.py:76:9: F405 'goto' may be undefined, or defined from star imports: random, turtle
memory.py:77:9: F405 'color' may be undefined, or defined from star imports: random, turtle
memory.py:78:9: F405 'write' may be undefined, or defined from star imports: random, turtle
memory.py:80:5: F405 'update' may be undefined, or defined from star imports: random, turtle
memory.py:81:5: F405 'ontimer' may be undefined, or defined from star imports: random, turtle
memory.py:84:1: F405 'shuffle' may be undefined, or defined from star imports: random, turtle
memory.py:85:1: F405 'setup' may be undefined, or defined from star imports: random, turtle
memory.py:86:1: F405 'addshape' may be undefined, or defined from star imports: random, turtle
memory.py:87:1: F405 'hideturtle' may be undefined, or defined from star imports: random, turtle
memory.py:88:1: F405 'tracer' may be undefined, or defined from star imports: random, turtle
memory.py:89:1: F405 'onscreenclick' may be undefined, or defined from star imports: random, turtle
memory.py:91:1: F405 'done' may be undefined, or defined from star imports: random, turtle

Cambios para correguir los errores:
from random import shuffle
from turtle import up, goto, down, color, begin_fill, forward, left, end_fill
from turtle import stamp, write, update, ontimer, setup, addshape, clear
from turtle import hideturtle, tracer, onscreenclick, done, shape

Explicacion de los cambios:
Se agregaron librerias especificas para evitar usar "*" y traer librerias que no se van a ocupar

Validacion despues de cambios en los imports:
C:\Users\julio\OneDrive\Desktop\Escuela\TC1001S\Proyecto_Equipo4\Juego_Memoria>python -m flake8 memory.py

Cambios:
def tap(x, y):
    """Actualice la marca y los mosaicos ocultos según el toque
    Agregamos una variable global counter para contar los taps
    e imprimirlos en la consola"""
    global counter
    spot = index(x, y)
    mark = state['mark']

    if mark is None or mark == spot or tiles[mark] != tiles[spot]:
        state['mark'] = spot
    else:
        hide[spot] = False
        hide[mark] = False
        state['mark'] = None
        counter += 1
        print('Taps: ' + str(counter))
    """Imprime un mensaje cuando todas las casillas esten completas"""
    if all(not i for i in hide):
        print('¡Juego terminado!')
        tracer(True)

Validacion despues de agregar las actividades:
C:\Users\julio\OneDrive\Desktop\Escuela\TC1001S\Proyecto_Equipo4\Juego_Memoria>python -m flake8 memory.py

Explicacion de los cambios:
Se agrego la variable counter para contar los taps.
La linea "counter += 1" nos ayuda a sumar las veces que se hace tap
Las lines "if all(not i for i in hide):
        print('¡Juego terminado!')
        tracer(True)"
nos ayudan a ver si ya se completo el juego y cuando lo completan se imprime "Juego terminado"

