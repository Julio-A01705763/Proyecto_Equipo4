"""Tic Tac Toe
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

board = [False for i in range(9)]  # detect if checkbox is already used

diff = 130 - SIZE  # Difference between grid and icon size


def grid():  # define the grid
    """Draw tic-tac-toe grid."""
    line(-67, 200, -67, -200)
    line(67, 200, 67, -200)
    line(-200, -67, 200, -67)
    line(-200, 67, 200, 67)


def drawx(x, y):  # Draw the x in the window
    """Draw X player."""
    line(x+diff, y + SIZE, x + SIZE, y+diff)
    line(x+diff, y+diff, x + SIZE, y + SIZE)


def drawo(x, y):  # Draw the x in the window
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


def tap(x, y):  # User click location
    """Draw X or O in tapped square."""
    x = floor(x)
    y = floor(y)

    # Corresponding index of the square pressed
    ind = int((x+200)//133+(abs(y-66))//133*3)

    # Check if the box is occupied
    if not board[ind]:
        board[ind] = True
        player = state['player']
        draw = players[player]
        draw(x, y)
        update()
        state['player'] = not player


setup(420, 420, 370, 0)  # Create the window
hideturtle()
tracer(False)

# Makes the grid and detect the clicks
grid()
update()
onscreenclick(tap)
done()
