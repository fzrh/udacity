import turtle
def draw_shapes():
    window = turtle.Screen()
    window.bgcolor('white')

    draw_square()
    draw_circle()
    draw_triangle()

    window.exitonclick()

def draw_square():
    matt = turtle.Turtle()
    matt.shape('turtle')
    matt.color('black')
    matt.speed(2)
    i = 0
    while (i < 4):
        matt.forward(100)
        matt.right(90)
        i = i + 1

def draw_circle():
    ailee = turtle.Turtle()
    ailee.shape('arrow')
    ailee.color('red')
    ailee.circle(100)

def draw_triangle():
    taeyang = turtle.Turtle()
    taeyang.shape('arrow')
    taeyang.color('brown')
    i = 0
    while (i < 3):
        taeyang.forward(60)
        taeyang.left(120)
        i = i + 1

draw_shapes()
