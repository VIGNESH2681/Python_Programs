import random
from turtle import Turtle
tom=Turtle()
colors=["red","blue","green","pink","brown","black","orange","yellow","violet","dark blue","DarkOrange","gold","ivory"]
for i in range(3,9): #3,4,5,6,7,8
    angle=360/i
    tom.pencolor(random.choice(colors))
    for _ in range(i): #0,1,2
        tom.forward(100)
        tom.right(angle)
tom.screen.mainloop()


