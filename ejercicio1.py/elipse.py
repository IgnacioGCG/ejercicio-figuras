import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Crear un objeto turtle
t = turtle.Turtle()

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