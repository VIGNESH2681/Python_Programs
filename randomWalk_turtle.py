import turtle
from turtle import Turtle
import random
direction=[0,90,180,270]
turtle.colormode(255)
tom=Turtle()
tom.width(10)
tom.shape("turtle")
for _ in range(50):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tom.seth(random.choice(direction))
    # tom.setheading(random.randrange(0,360,90)) # 0 90 180 270 360
    tom.pencolor((r,g,b))
    tom.forward(30)
tom.screen.mainloop()

