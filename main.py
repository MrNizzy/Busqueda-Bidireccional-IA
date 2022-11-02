import turtle
import time
import numpy as np
import config
import setup_path

# Window configuration
width = 800
height = 800

# Size of grid boxes (Affects movements, and correct responsive positioning).
# Recommended: 50
paddingBox = 50

# The initial position of the player.
playerCoord = config.playerCoords

# The initial position of the target.
metaCoord = config.metaCoords

# Cumulated movement cost
cost = 0

# Loading of the board via .txt file
# Accepts only square matrices, i.e. NxN and not NxM
board = np.loadtxt("./board.txt", delimiter=" ")

# Matrix size for configurations. Do not modify.
boardSize = len(board)

# Setting the window
window = turtle.Screen()
window.title("Artificial intelligence")
window.setworldcoordinates((-width/4),(-height/4),width,height)
window.bgcolor("#000000")
window.tracer(0)

# Add new figures with images, only .gif accepted
window.addshape('./assets/agent.gif')
window.addshape('./assets/chest.gif')
window.addshape('./assets/meta.gif')
window.addshape('./assets/wall.gif')

# Agent
size = 4.0
print("\nInitial coordinate: " + str(playerCoord))
player = turtle.Turtle()
player.penup()
player.speed(6)
player.shape('./assets/agent.gif')
player.shapesize(size - 0.5)
# Sets the initial position of the player with respect to the position declared in the matrix.
player.goto((paddingBox / 2)+(playerCoord[0]*paddingBox),((boardSize*paddingBox - (paddingBox / 2)) - (playerCoord[1]*paddingBox)))
player.direction = "stop"

# Meta
meta = turtle.Turtle()
meta.penup()
meta.speed(0)
meta.shape("./assets/chest.gif")
meta.shapesize(size - 0.5)
# Sets the initial position of the target with respect to the declared position in the matrix.
meta.goto(((paddingBox / 2)+(metaCoord[0]*paddingBox)),((boardSize*paddingBox - (paddingBox / 2)) - (metaCoord[1]*paddingBox)))

# Setup Grid
grid = turtle.Turtle()
grid.pensize(2)
grid.color("#C8D8EE")
grid.penup()
grid.goto(0,0)
grid.pendown()

# Walls
wall = turtle.Turtle()
wall.penup()
wall.shape('./assets/wall.gif')
wall.shapesize(1.3,1.7)
wall.color("#FFFFFF")
wall.goto((paddingBox / 2), (paddingBox * boardSize) - (paddingBox / 2))

def generateWalls(n,matrix):
    """
    It goes through the matrix and if it finds a 1, it stamps a wall in the corresponding position
    
    :param n: size of the maze
    :param matrix: The matrix that contains the walls
    """
    for i in range(n):
        for j in range(n):
            wall.goto((paddingBox / 2), (paddingBox * n) - (paddingBox / 2))
            if(matrix[j][i] == 1):
                wall.goto(i*paddingBox+wall.xcor(), wall.ycor()-(j*paddingBox))
                wall.stamp()
generateWalls(boardSize,board)

def generateGrid(n,size):
    """
    It draws a grid of n by n squares, each of size size, with a padding of paddingBox between each
    square
    
    :param n: number of boxes in the grid
    :param size: The size of each box in the grid
    """
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

def isMeta():
    """
    If the player is at the same position as the treasure, then the treasure is shown and the player is
    hidden. Otherwise, the treasure is hidden and the player is shown and also calculates 
    the accumulated cost for each player's move.
    :return: a boolean value.
    """
    global cost
    cost = cost + 1
    print("Cumulative current cost: " + str(cost))
    if(meta.position() == player.position()):
        meta.shape("./assets/meta.gif")
        player.hideturtle()
        return True
    else:
        meta.shape("./assets/chest.gif")
        player.showturtle()
        return False

# Player movement, also valid that does not go off the board.
def up():
    """
    Moves the player one position up
    """
    y = player.ycor()
    if(y < (boardSize*paddingBox)-paddingBox):
        player.sety(y + paddingBox)
        #print(player.position())
        isMeta()

def down():
    """
    Moves the player one position down
    """
    y = player.ycor()
    if(y > (paddingBox / 2)):
        player.sety(y - paddingBox)
        #print(player.position())
        isMeta()

def left():
    """
    Moves the player one position left
    """
    x = player.xcor()
    if(x > (paddingBox / 2)):
        player.setx(x - paddingBox)
        #print(player.position())
        isMeta()

def right():
    """
    Moves the player one position right
    """
    x = player.xcor()
    if(x < (boardSize*paddingBox)-paddingBox):
        player.setx(x + paddingBox)
        #print(player.position())
        isMeta()

def pathAuto():
    """
    It takes the path from the file setup_path.py and moves the player along the path.
    """
    pathBdBFS = setup_path.bd_path
    xPos = playerCoord[1]
    yPos = playerCoord[0]
    # Converts the path to non-repeating single values of the array to avoid returning
    #path = np.unique(pathBdBFS, axis=0)
    path = pathBdBFS

    # It is a for that moves the player automatically, following the path that is in the 
    # file path.txt.
    for i in range(len(path)):
        if(yPos < path[i][1]):
            print(path[i])
            right()
            yPos+=1
        elif (xPos < path[i][0]):
            print(path[i])
            down()
            xPos+=1
        elif (yPos > path[i][1]):
            print(path[i])
            left()
            yPos-=1
        elif (xPos > path[i][0]):
            print(path[i])
            up()
            xPos-=1
        time.sleep(1)
        window.update()
pathAuto()

# keyboard listeners, arrow keys ↑ ↓ ← ← →
window.listen()
window.onkey(up,"Up")
window.onkey(down,"Down")
window.onkey(left,"Left")
window.onkey(right,"Right")

# Automatic update of the window.
while True:
    window.update()