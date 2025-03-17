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
    
# Dibujar un círculo
t.penup()
t.goto(-100, 0)
t.pendown()
draw_circle(50, "red")

# Ocultar el objeto turtle y mostrar la ventana
t.hideturtle()
turtle.done()