import turtle as t
import random 
timmy = t.Turtle()
t.colormode(255)

timmy.speed(100)
timmy.width(1)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_color = (r,g,b)
    return random_color

direction = [0, 90, 180, 270]
for move in range(40):
    timmy.circle(90)
    timmy.right(10)
    # timmy.setheading(random.choice(direction))
    timmy.pencolor(random_color())

screen = t.Screen()
screen.exitonclick()




