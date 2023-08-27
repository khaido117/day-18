from turtle import Turtle, Screen, colormode
import random
colormode(255)

color_list = [(202,164,109),(238,240,245),(102,168,109),(18,10,145,),(18,20,145),(255,10,145)]

tim = Turtle()
tim.speed(10)
tim.color("")
tim.goto(-300,-200)

for _ in range(10):
    for _ in range(10):
        tim.dot(20, random.choice(color_list))
        tim.forward(50)
    tim.left(90)
    tim.forward(50)
    tim.left(90)
    tim.forward(500)
    tim.left(180)

windown = Screen()
windown.exitonclick()


