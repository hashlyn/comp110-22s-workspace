from turtle import Turtle, colormode, done 
colormode(255)
leo: Turtle = Turtle()

leo.penup()
leo.goto(-150, -45)
leo.pendown()

leo.fillcolor(128, 128, 128) 
leo.begin_fill()
leo.speed(50)
i: int = 0
while i < 3:
    leo.forward(300)
    leo.left(120)
    i += 1
leo.end_fill()
leo.ht()
done()

bob: Turtle = Turtle()

bob.color(0, 0, 0)
bob.penup()
bob.goto(-150, -45)
bob.pendown()
bob.speed(75)

i: int = 0 
while i < 3: 
    bob.forward(300)
    bob.left(90)
    i += 1 
bob.ht()

side_length: int = 300 
i: int = 0
while i < 300: 
    bob.forward(side_length)
    bob.left(120)
    side_length = side_length * 0.96 
    i += 1
done()