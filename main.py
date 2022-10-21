import turtle
import numpy as np

# Window configuration
width = 800
height = 800

# Size of grid boxes (Affects movements, and correct responsive positioning).
# Recommended: 50
paddingBox = 50

# Setting the window
window = turtle.Screen()
window.title("Artificial intelligence")
window.setworldcoordinates((-width/4),(-height/4),width,height)
window.bgcolor("#000000")
window.tracer(0)

# Add new figures with images, only .gif accepted
window.addshape('agent.gif')
window.addshape('chest.gif')
window.addshape('meta.gif')
window.addshape('wall.gif')

# Loading of the board via .txt file
# Accepts only square matrices, i.e. NxN and not NxM
board = np.loadtxt("./board.txt", delimiter=" ")
# Matrix size for configurations. Do not modify.
boardSize = len(board)

# Search for elements in the matrix, to know their coordinates.
def searchItem(item):
    for i in range(boardSize):
        for j in range(boardSize):
            if board[j][i] == item:
                return np.array((j,i))

# Agent
size = 4.0
playerCoord = [1,1]
print(playerCoord)
player = turtle.Turtle()
player.penup()
player.speed(6)
player.shape('agent.gif')
player.shapesize(size - 0.5)
# Sets the initial position of the player with respect to the position declared in the matrix.
player.goto((paddingBox / 2)+(playerCoord[0]*paddingBox),((boardSize*paddingBox - (paddingBox / 2)) - (playerCoord[1]*paddingBox)))
player.direction = "stop"

# Meta
metaCoord = [10, 10]
meta = turtle.Turtle()
meta.penup()
meta.speed(0)
meta.shape("chest.gif")
meta.shapesize(size - 0.5)
# Sets the initial position of the target with respect to the declared position in the matriz.
meta.goto(((paddingBox / 2)+(metaCoord[0]*paddingBox)),((boardSize*paddingBox - (paddingBox / 2)) - (metaCoord[1]*paddingBox)))

# Walls
wall = turtle.Turtle()
wall.penup()
wall.shape('wall.gif')
wall.shapesize(1.3,1.7)
wall.color("#FFFFFF")
wall.goto((paddingBox / 2), (paddingBox * boardSize) - (paddingBox / 2))

# Cumulated movement cost
cost = 0

# It identifies whether the goal is reached, if so, it changes the icon and also calculates 
# the accumulated cost for each player's move.
def isMeta():
    global cost
    cost = cost + 1
    print("Cumulative current cost: " + str(cost))
    if(meta.position() == player.position()):
        meta.shape("meta.gif")
        player.hideturtle()
        return True
    else:
        meta.shape("chest.gif")
        player.showturtle()
        return False


def generateWalls(n,matriz):
    for i in range(n):
        for j in range(n):
            wall.goto((paddingBox / 2), (paddingBox * n) - (paddingBox / 2))
            if(matriz[i][j] == 1):
                wall.goto(i*paddingBox+wall.xcor(), wall.ycor()-(j*paddingBox))
                wall.stamp()
generateWalls(boardSize,board)

# Setup Grid
grid = turtle.Turtle()
grid.pensize(2)
grid.color("#C8D8EE")
grid.penup()
grid.goto(0,0)
grid.pendown()

# Automatic generation of the grid (grid of lines) depending on the size of the matrix.
def generateGrid(n,size):
    for i in range(n+1):
        if (grid.xcor() == 0 and grid.ycor() == 0):
            grid.goto(grid.xcor(),(size*n))
        elif(grid.ycor() == 0):
            grid.goto(grid.xcor()+paddingBox,grid.ycor())
            grid.goto(grid.xcor(),grid.ycor()+(size*n))
        elif (grid.ycor() != 0):
            grid.goto(grid.xcor()+paddingBox,grid.ycor())
            grid.goto(grid.xcor(),grid.ycor()-(size*n))
    grid.penup()
    grid.goto(0,0)
    grid.pendown()
    for i in range(n+1):
        if (grid.xcor() == 0 and grid.ycor() == 0):
            grid.goto((size*n),grid.ycor())
        elif(grid.xcor() == 0):
            grid.goto(grid.xcor(),grid.ycor()+paddingBox)
            grid.goto(grid.xcor()+(size*n),grid.ycor())
        elif (grid.xcor() != 0):
            grid.goto(grid.xcor(),grid.ycor()+paddingBox)
            grid.goto(grid.xcor()-(size*n),grid.ycor())
generateGrid(boardSize,paddingBox)
grid.hideturtle()

# Player movement, also valid that does not go off the board.
def up():
    y = player.ycor()
    if(y < (boardSize*paddingBox)-paddingBox):
        player.sety(y + paddingBox)
        print(player.position())
        isMeta()
def down():
    y = player.ycor()
    if(y > (paddingBox / 2)):
        player.sety(y - paddingBox)
        print(player.position())
        isMeta()
def left():
    x = player.xcor()
    if(x > (paddingBox / 2)):
        player.setx(x - paddingBox)
        print(player.position())
        isMeta()
def right():
    x = player.xcor()
    if(x < (boardSize*paddingBox)-paddingBox):
        player.setx(x + paddingBox)
        print(player.position())
        isMeta()

# keyboard listeners, arrow keys ↑ ↓ ← ← →
window.listen()
window.onkey(up,"Up")
window.onkey(down,"Down")
window.onkey(left,"Left")
window.onkey(right,"Right")

# Automatic update of the window.
while True:
    window.update()