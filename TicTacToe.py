"""Tic Tac Toe
Exercises
1. Give the X and O a different color and width.
2. What happens when someone taps a taken spot?
3. How would you detect when someone has won?
4. How could you create a computer player?
"""
from freegames import line
from turtle import circle
from turtle import done
from turtle import down
from turtle import goto
from turtle import hideturtle
from turtle import onscreenclick
from turtle import setup
from turtle import tracer
from turtle import up
from turtle import update

SIZE = 100

board = [False for i in range(9)]  # detectar si ya está usada la casilla

diff = 130 - SIZE  # Diferencia entre el tamaño de la cuadrícula y el icono


def grid():  #Define la cuadricula
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):  # Dibuja la x en la ventana
    """Draw X player."""
    line(x+diff, y + SIZE, x + SIZE, y+diff)
    line(x+diff, y+diff, x + SIZE, y + SIZE)


def drawo(x, y):  # Dibuja la x en la ventana
    """Draw O player."""
    up()
    goto(x + 67, y + diff//2)
    down()
    circle(SIZE//2)


def floor(value): 
    """Round value down to grid with square size 133."""
    return ((value + 200) // 133) * 133 - 200


state = {'player': 0}
players = [drawx, drawo]


def tap(x, y): # Ubicación del click del usuario
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    # Indice correspondiente del cuadrado pulsado
    ind = int((x+200)//133+(abs(y-66))//133*3)

    # Checa si la casilla está ocupada
    if not board[ind]:
        board[ind] = True
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player


setup(420, 420, 370, 0)  # Crea la ventana
hideturtle()
tracer(False)
# Hace la cuadricula
grid()
update()
onscreenclick(tap)  # Detecta los clicks
done()