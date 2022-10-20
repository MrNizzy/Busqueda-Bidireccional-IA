import turtle
import numpy as np

#Configuración de la ventana
ancho = 800
alto = 800

# Tamaño de los cuadros de la grilla (Afecta a los movimientos, y posicionamiento correcto responsive).
# Recomendado: 150
paddingBox = 150

# Estableciendo la ventana
window = turtle.Screen()
window.title("Inteligencia artificial")
window.setworldcoordinates((-ancho/4),(-alto/4),ancho,alto)
window.bgcolor("#000000")
window.tracer(0)

#Añadir nuevas figuras con imágenes, solo acepta .gif
window.addshape('agent.gif')
window.addshape('chest.gif')
window.addshape('meta.gif')

# Carga del tablero mediante el archivo .txt
# Solo acepta matrices cuadradas, es decir, NxN y no NxM
tablero = np.loadtxt("./tablero.txt", delimiter=" ")
# Tamaño de la matriz para configuraciones. No modificar.
tableroSize = len(tablero)

# Busca elementos en la matriz, para conocer sus coordenadas.
def searchItem(item):
    for i in range(tableroSize):
        for j in range(tableroSize):
            if tablero[j][i] == item:
                return np.array((j,i))

#Agente
size = 4.0
playerCoord = searchItem(1)
print(playerCoord)
player = turtle.Turtle()
player.penup()
player.speed(6)
player.shape('agent.gif')
player.shapesize(size - 0.5)
# Configura la posición inicial del jugador respecto a la posición declarada en la matriz.
player.goto((paddingBox / 2)+(playerCoord[0]*paddingBox),((tableroSize*paddingBox - (paddingBox / 2)) - (playerCoord[1]*paddingBox)))
player.direction = "stop"

#Meta
metaCoord = searchItem(2)
meta = turtle.Turtle()
meta.penup()
meta.speed(0)
meta.shape("chest.gif")
meta.shapesize(size - 0.5)
# Configura la posición inicial de la meta respecto a la posición declarada en la matriz.
meta.goto((paddingBox / 2)+(metaCoord[0]*paddingBox),((tableroSize*paddingBox - (paddingBox / 2)) - (metaCoord[1]*paddingBox)))

#Costo de movimientos acumulado
costo = 0

# Identifica si se llega a la meta, de ser así, cambia el icono y además cálcula el costo
# acumulado por cada movimiento del jugador.
def isMeta():
    global costo
    costo = costo + 1
    print("Costo actual acumulado: " + str(costo))
    if(meta.position() == player.position()):
        meta.shape("meta.gif")
        player.hideturtle()
        return True
    else:
        meta.shape("chest.gif")
        player.showturtle()
        return False

#Grilla
grilla = turtle.Turtle()
grilla.pensize(2)
grilla.color("#C8D8EE")
grilla.penup()
grilla.goto(0,0)
grilla.pendown()

# Generación automatica de la grilla (malla de líneas) dependiendo del tamaño de la matriz.
def generateGrid(n,size):
    for i in range(n+1):
        if (grilla.xcor() == 0 and grilla.ycor() == 0):
            grilla.goto(grilla.xcor(),(size*n))
        elif(grilla.ycor() == 0):
            grilla.goto(grilla.xcor()+paddingBox,grilla.ycor())
            grilla.goto(grilla.xcor(),grilla.ycor()+(size*n))
        elif (grilla.ycor() != 0):
            grilla.goto(grilla.xcor()+paddingBox,grilla.ycor())
            grilla.goto(grilla.xcor(),grilla.ycor()-(size*n))
    grilla.penup()
    grilla.goto(0,0)
    grilla.pendown()
    for i in range(n+1):
        if (grilla.xcor() == 0 and grilla.ycor() == 0):
            grilla.goto((size*n),grilla.ycor())
        elif(grilla.xcor() == 0):
            grilla.goto(grilla.xcor(),grilla.ycor()+paddingBox)
            grilla.goto(grilla.xcor()+(size*n),grilla.ycor())
        elif (grilla.xcor() != 0):
            grilla.goto(grilla.xcor(),grilla.ycor()+paddingBox)
            grilla.goto(grilla.xcor()-(size*n),grilla.ycor())
generateGrid(tableroSize,paddingBox)
grilla.hideturtle()

#Movimiento del jugador, también válida que no se salga del tablero.
def up():
    y = player.ycor()
    if(y < (tableroSize*paddingBox)-paddingBox):
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
    if(x < (tableroSize*paddingBox)-paddingBox):
        player.setx(x + paddingBox)
        print(player.position())
        isMeta()

# Listeners del teclado, teclas de flechas ↑ ↓ ← →
window.listen()
window.onkey(up,"Up")
window.onkey(down,"Down")
window.onkey(left,"Left")
window.onkey(right,"Right")

# Actualización automatica de la ventana.
while True:
    window.update()