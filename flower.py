# import turtle
# import math

# screen = turtle.Screen()
# screen.bgcolor("black")
# screen.title("Animated Starburst Pattern")

# t = turtle.Turtle()
# t.speed(5)
# t.hideturtle()
# t.penup()

# points = 1500

# for i in range(points):
#     angle = (i / points) * 2 * math.pi

#     r = 150 * (1 + 0.6 * math.cos(20 * angle)) 
#     x = r * math.cos(angle)
#     y = r * math.sin(angle)

#     pink_val = 1.0
#     yellow_val = i / points
#     t.color(pink_val, yellow_val, 1 * (1 - yellow_val))  

#     t.goto(x, y)
#     t.dot(3) 

# turtle.done()

import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Animated Starburst Pattern")

screen.tracer(0, 0)

t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

points = 1500

for i in range(points):
    angle = (i / points) * 2 * math.pi
    
    r = 150 * (1 + 0.6 * math.cos(20 * angle))
    x = r * math.cos(angle)
    y = r * math.sin(angle)
    
    pink_val = 1.0
    yellow_val = i / points
    t.color(pink_val, yellow_val, 1 * (1 - yellow_val))
    
    t.goto(x, y)
    t.dot(3)
    
    # Har 5 ta nuqtada ekranni yangilaymiz (tezlik biroz sekinlashadi)
    if i % 5 == 0:
        screen.update()

screen.update()

turtle.done()