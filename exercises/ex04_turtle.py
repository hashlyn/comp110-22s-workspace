"""A quaint little field house."""

__author__ = "730412456"

from turtle import Turtle, colormode, done, tracer, update
colormode(255)
MAX_SPEED: int = 0


def main() -> None:
    """The entrypoint of my scene."""
    tracer(0, 0)
    matthew: Turtle = Turtle() 
    matthew.fillcolor(194, 223, 230)
    matthew.begin_fill()
    matthew.speed(MAX_SPEED)
    draw_square(matthew, -300, 300, 600)
    matthew.end_fill()
    matthew.fillcolor(134, 149, 97)
    matthew.begin_fill()
    matthew.speed(MAX_SPEED)
    draw_square(matthew, -300, 0, 600)
    matthew.end_fill()
    matthew.fillcolor(240, 171, 154) 
    matthew.begin_fill()
    matthew.speed(MAX_SPEED)
    draw_square(matthew, -100, 100, 200)
    matthew.end_fill()
    matthew.ht()
    brianna: Turtle = Turtle()
    draw_triangle(brianna, -100, 100, 200)
    brianna.ht()
    harry: Turtle = Turtle()
    vertical_rectangle(harry, -75, -100, 100)
    i: int = 0
    x: float = -300
    y: float = -200
    while i < 13: 
        vertical_rectangle(harry, x, y, 40)
        x += 42.0
        i += 1
    harry.ht()
    nyla: Turtle = Turtle() 
    nyla.pencolor(111, 92, 69)
    nyla.penup()
    nyla.goto(-300, -190)
    nyla.pendown()
    nyla.forward(525)
    nyla.penup()
    nyla.goto(-300, -170)
    nyla.pendown()
    nyla.forward(525)
    nyla.ht()
    george: Turtle = Turtle()
    george.fillcolor(241, 140, 112)
    george.begin_fill()
    george.speed(MAX_SPEED)
    counter: int = 0
    width: float = 50
    while counter < 2: 
        draw_square(george, 15, 70, width)
        george.end_fill()
        width = width - 10.0
        counter += 1
        george.fillcolor(209, 234, 238)
        george.begin_fill()
    george.ht()
    squirtle: Turtle = Turtle()
    squirtle.pencolor(241, 205, 112)
    squirtle.fillcolor(241, 205, 112)
    squirtle.begin_fill()
    squirtle.speed(MAX_SPEED)
    squirtle.penup()
    squirtle.goto(-200, 170)
    squirtle.pendown()
    squirtle.circle(40)
    squirtle.end_fill()
    squirtle.ht()
    lily: Turtle = Turtle()
    lily.speed(MAX_SPEED)
    draw_flower_ball(lily, 20, -110)
    lily.ht()
    update()
    done()
    

def draw_square(some_turtle: Turtle, x: float, y: float, width: float) -> None: 
    """Draw a square of the given width whose top-left corner is located at x, y."""
    some_turtle.penup()
    some_turtle.goto(x, y)
    some_turtle.pendown
    i: int = 0 
    while i < 4: 
        some_turtle.forward(width)
        some_turtle.right(90)
        i += 1 


def draw_triangle(some_turtle: Turtle, x: float, y: float, width: float) -> None: 
    """Draw a triangle whose bottom-left corner is located at x, y."""
    some_turtle.fillcolor(96, 96, 96)
    some_turtle.begin_fill()
    some_turtle.speed(MAX_SPEED)
    some_turtle.penup()
    some_turtle.goto(x, y) 
    some_turtle.setheading(0.0)
    some_turtle.pendown 
    i: int = 0 
    while i < 3: 
        some_turtle.forward(width)
        some_turtle.left(120)
        i += 1 
    some_turtle.end_fill()


def vertical_rectangle(some_turtle: Turtle, x: float, y: float, width: float) -> None: 
    """Draw a vertical rectangle whose bottom-left corner is located at x, y."""
    some_turtle.fillcolor(111, 92, 69) 
    some_turtle.begin_fill()
    some_turtle.speed(MAX_SPEED)
    some_turtle.penup()
    some_turtle.goto(x, y)
    some_turtle.setheading(0.0)
    some_turtle.pendown
    some_turtle.forward(width / 2)
    some_turtle.left(90)
    some_turtle.forward(width) 
    some_turtle.left(90)
    some_turtle.forward(width / 2)
    some_turtle.left(90)
    some_turtle.forward(width)
    some_turtle.end_fill()


def draw_flower_ball(some_turtle: Turtle, x: float, y: float) -> None: 
    """Draw a flower in the shape of a ball located at x, y."""
    some_turtle.penup()
    some_turtle.goto(x, y)
    some_turtle.pendown
    from random import randint
    color: int = randint(0, 3)
    if color == 0: 
        some_turtle.fillcolor(178, 141, 203)
    elif color == 1:
        some_turtle.fillcolor(233, 224, 83)
    elif color == 2: 
        some_turtle.fillcolor(52, 178, 177)
    else: 
        some_turtle.fillcolor(211, 113, 168)
    some_turtle.begin_fill()
    some_turtle.circle(10)
    some_turtle.end_fill()


if __name__ == "__main__": 
    print("__name__is '__main__'")
    main()