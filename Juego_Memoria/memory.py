"""
Autor de los cambios: Julio Cesar Peres Rodriguez
Fecha: 24-03-2023
Mateira: TC1001S

Memorama, rompecabezas de números pares.

Actividades:

1. Contar y desplegar el numero de taps
2.Detectar cuando todos los cuadros se han destapado
"""

from random import shuffle
from turtle import up, goto, down, color, begin_fill, forward, left, end_fill
from turtle import stamp, write, update, ontimer, setup, addshape, clear
from turtle import hideturtle, tracer, onscreenclick, done, shape

from freegames import path

car = path('car.gif')
tiles = list(range(32)) * 2
state = {'mark': None}
hide = [True] * 64
counter = 0


def square(x, y):
    """Dibuja un cuadrado blanco con contorno negro en (x, y)."""
    up()
    goto(x, y)
    down()
    color('black', 'white')
    begin_fill()
    for count in range(4):
        forward(50)
        left(90)
    end_fill()


def index(x, y):
    """Convierta las coordenadas (x, y) en índice de mosaicos."""
    return int((x + 200) // 50 + ((y + 200) // 50) * 8)


def xy(count):
    """Convierta el recuento de mosaicos en coordenadas (x, y)."""
    return (count % 8) * 50 - 200, (count // 8) * 50 - 200


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


def draw():
    """Dibujar imagen y mosaicos."""
    clear()
    goto(0, 0)
    shape(car)
    stamp()

    for count in range(64):
        if hide[count]:
            x, y = xy(count)
            square(x, y)

    mark = state['mark']

    if mark is not None and hide[mark]:
        x, y = xy(mark)
        up()
        goto(x + 2, y)
        color('black')
        write(tiles[mark], font=('Arial', 30, 'normal'))

    update()
    ontimer(draw, 100)


shuffle(tiles)
setup(420, 420, 370, 0)
addshape(car)
hideturtle()
tracer(False)
onscreenclick(tap)
draw()
done()
