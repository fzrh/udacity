import turtle
def draw_square(some_turtle):
    i = 0
    while (i < 4):
        some_turtle.forward(100)
        some_turtle.right(90)
        i = i + 1

def draw_circle_art():
    window = turtle.Screen()
    window.bgcolor('white')

    nick = turtle.Turtle()
    nick.shape('turtle')
    nick.color('black')
    nick.speed(2)
    for i in range(1,37):
        draw_square(nick)
        nick.right(10)

    window.exitonclick()

draw_circle_art()
