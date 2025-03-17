import turtle

# Configuración de la pantalla
screen = turtle.Screen()
screen.bgcolor("white")

# Crear un objeto turtle
t = turtle.Turtle()

# Función para dibujar un cuadrado
def draw_square(side_length, color):
    t.color(color)
    t.begin_fill()
    for _ in range(4):
        t.forward(side_length)
        t.right(90)
    t.end_fill()
    
# Dibujar un cuadrado
t.penup()
t.goto(0, 0)
t.pendown()
draw_square(100, "blue")

# Ocultar el objeto turtle y mostrar la ventana
t.hideturtle()
turtle.done()