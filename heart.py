import math
import random
import turtle

# Ekran sozlamalari
screen = turtle.Screen()
screen.setup(width=800, height=800)
screen.bgcolor("#000000")
screen.title("LOVE YOU Heart")
screen.tracer(0)  # Tasvirni juda tez va silliq chizish uchun

# Chizuvchi obyekt (turtle)
t = turtle.Turtle()
t.hideturtle()
t.penup()

TEXT = "LOVE YOU"
PINK = "#F72E53"
SHADOW = "#F3A5B1"

def get_heart_points():
    points = []
    
    # Tashqi kontur
    for i in range(180):
        a = (i / 180) * math.pi * 2
        x = 16 * (math.sin(a) ** 3)
        y = -(13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a))
        
        # Turtle koordinatasiga moslash (y o'qi teskari bo'lgani uchun -y)
        points.append({
            "x": x * 18,
            "y": -y * 18,
            "delay": random.randint(0, 100),
            "visible": False
        })

    # Ichki qatlamlar
    for s in [0.2, 0.4, 0.6, 0.8]:
        for i in range(60):
            a = (i / 60) * math.pi * 2
            x = 16 * (math.sin(a) ** 3)
            y = -(13 * math.cos(a) - 5 * math.cos(2 * a) - 2 * math.cos(3 * a) - math.cos(4 * a))
            
            points.append({
                "x": x * 18 * s,
                "y": -y * 18 * s,
                "delay": random.randint(0, 150),
                "visible": False
            })

    return points

points = get_heart_points()
frame = 0

# Animatsiya sikli
def draw():
    global frame
    t.clear()
    
    for p in points:
        # Nuqtalar sekin-asta miltillab paydo bo'lishi uchun
        if frame > p["delay"]:
            p["visible"] = True
            
        if p["visible"]:
            t.goto(p["x"], p["y"])
            t.color(PINK)
            t.write(TEXT, align="center", font=("Consolas", 8, "bold"))
            
    screen.update()
    frame += 1
    screen.ontimer(draw, 20) # 20 ms interval bilan yangilash

# Animatsiyani boshlash
draw()

# Oyna yopilib ketmasligi uchun
turtle.done()