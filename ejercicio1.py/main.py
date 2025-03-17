import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Crear un objeto turtle
t = turtle.Turtle()

# Función para dibujar un círculo
def draw_circle(radius, color):
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Función para dibujar un cuadrado
def draw_square(side_length, color):
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(side_length)
        t.right(90)
    t.end_fill()

# Dibujar un círculo
t.penup()
t.goto(-100, 0)
t.pendown()
draw_circle(50, "red")

# Dibujar un cuadrado
t.penup()
t.goto(0, 0)
t.pendown()
draw_square(100, "blue")

# Dibujar otro círculo
t.penup()
t.goto(150, 0)
t.pendown()
draw_circle(50, "green")

# Función para dibujar una elipse
def draw_ellipse(radius1, radius2, color):
    t.color(color)
    t.begin_fill()
    t.left(45)
    for _ in range(2):
        t.circle(radius1, 90)
        t.circle(radius2, 90)
    t.end_fill()
    t.right(45)

# Dibujar una elipse
t.penup()
t.goto(0, -150)
t.pendown()
draw_ellipse(50, 100, "purple")

# Ocultar el objeto turtle y mostrar la ventana
t.hideturtle()
turtle.done()
# Función para dibujar una elipse
def draw_ellipse(radius1, radius2, color):
    t.color(color)
    t.begin_fill()
    t.left(45)
    for _ in range(2):
        t.circle(radius1, 90)
        t.circle(radius2, 90)
    t.end_fill()
    t.right(45)

# Dibujar una elipse
t.penup()
t.goto(0, -150)
t.pendown()
draw_ellipse(50, 100, "purple")