import turtle

#Configuración de la ventana
window = turtle.Screen()
window.title("Inteligencia artificial")
window.setup(width = 600, height = 600)
window.bgcolor("#000000")
window.tracer(0)

#Añadir nuevas figuras con imágenes, solo acepta .gif
window.addshape('agent.gif')
window.addshape('chest.gif')
window.addshape('meta.gif')

"""
titulo = turtle.Turtle()
titulo.write("Bienvenido", True, font=("Verdana", 28, "normal"), align="center")
titulo.penup()
titulo.goto(0,240)
"""

#Agente
size = 4.0
player = turtle.Turtle()
player.penup()
player.speed(6)
player.shape('agent.gif')
player.shapesize(size - 0.5)
player.goto(-120,120)
player.direction = "stop"

#Meta
meta = turtle.Turtle()
meta.penup()
meta.speed(0)
meta.shape("chest.gif")
meta.shapesize(size - 0.5)
meta.goto(120,-40)

#Costo de movimientos acumulado
costo = 0

def isMeta():
    global costo
    if(meta.position() == player.position()):
        meta.shape("meta.gif")
        player.hideturtle()
    else:
        meta.shape("chest.gif")
        player.showturtle()
    costo = costo + 1
    print("Costo actual acumulado: " + str(costo))

#Grilla
grilla = turtle.Turtle()
grilla.pensize(2)
grilla.color("#C8D8EE")
grilla.goto(-160,0)
grilla.goto(-160,160)
grilla.goto(160,160)
grilla.goto(160,80)
grilla.goto(-160,80)
grilla.goto(-160,0)
grilla.goto(160,0)
grilla.goto(160,-80)
grilla.goto(-160,-80)
grilla.goto(-160,160)
grilla.goto(-80,160)
grilla.goto(-80,-80)
grilla.goto(0,-80)
grilla.goto(0,160)
grilla.goto(80,160)
grilla.goto(80,-80)
grilla.goto(160,-80)
grilla.goto(160,160)
grilla.hideturtle()

#Movimiento
def up():
    y = player.ycor()
    if(y < 120):
        player.sety(y + (20 * size))
        print(player.position())
        isMeta()
def down():
    y = player.ycor()
    if(y > -40):
        player.sety(y - (20 * size))
        print(player.position())
        isMeta()
def left():
    x = player.xcor()
    if(x > -120):
        player.setx(x - (20 * size))
        print(player.position())
        isMeta()
def right():
    x = player.xcor()
    if(x < 80):
        player.setx(x + (20 * size))
        print(player.position())
        isMeta()

window.listen()
window.onkey(up,"Up")
window.onkey(down,"Down")
window.onkey(left,"Left")
window.onkey(right,"Right")

while True:
    window.update()