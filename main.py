import turtle
import time
import numpy as np

# Window configuration
width = 800
height = 800

# Size of grid boxes (Affects movements, and correct responsive positioning).
# Recommended: 50
paddingBox = 50
# The initial position of the player.
playerCoord = [1,1]
# The initial position of the target.
metaCoord = [10, 10]

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

def searchItem(item):
    """
    It takes an item and returns the position of that item in the board
    
    :param item: The item you want to find
    :return: the location of the item on the board.
    """
    for i in range(boardSize):
        for j in range(boardSize):
            if board[j][i] == item:
                return np.array((j,i))

def removeDuplicates(matrix):
    """
    For each sublist in the matrix, append the unique elements to a new sublist in the result matrix
    
    :param matrix: a list of lists
    :return: A list of lists.
    """
    res = []
    track = []
    count = 0
    
    for sub in matrix:
        res.append([]);
        for ele in sub:
            if ele not in track:
                res[count].append(ele)
                track.append(ele)
        count += 1
    return res

# Agent
size = 4.0
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
            if(matriz[j][i] == 1):
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

def pathAuto():
    """
    It loads the path from the file path.txt, and then it is getting the unique values from the path.
    Then, it is a for that moves the player automatically, following the path that is in the file
    path.txt
    """
    # Loading the path from the file path.txt, and then it is getting the unique values from the path.
    pathBdBFS = np.loadtxt("./path.txt",dtype="int")
    xPos = playerCoord[1]
    yPos = playerCoord[0]
    path = np.unique(pathBdBFS, axis=0)

    # It is a for that moves the player automatically, following the path that is in the 
    # file path.txt.
    for i in range(len(path)):
        if(yPos < path[i][1]):
            right()
            yPos+=1
        elif (xPos < path[i][0]):
            down()
            xPos+=1
        elif (yPos > path[i][1]):
            left()
            yPos-=1
        elif (xPos > path[i][0]):
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