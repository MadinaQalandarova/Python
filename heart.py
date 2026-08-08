import pygame
import math
import random
import sys

# Pygame-ni ishga tushirish
pygame.init()

# Ekran o'lchamlari
W, H = 800, 800
screen = pygame.display.set_mode((W, H))
pygame.display.set_caption("heart")
clock = pygame.time.Clock()

# Shrift va ranglar
font = pygame.font.SysFont("Consolas", 13)
TEXT = "LOVE YOU"
PINK = (255, 77, 109)
BG = (5, 5, 5)

def heart_points():
    points = []
    cx, cy = W // 2, H // 2
    scale = min(W, H) / 45

    # Tashqi kontur (yurakning atrofi)
    for i in range(180):
        t = (i / 180) * math.pi * 2
        x = 16 * math.pow(math.sin(t), 3)
        y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
        
        points.append({
            "x": cx + x * scale,
            "y": cy + y * scale,
            "alpha": 0,
            "target": random.uniform(180, 255),
            "delay": random.uniform(0, 6000),
        })

    # Ichki qatlamlar (yurakning ichki qismi)
    for s in [0.2, 0.4, 0.6, 0.8]:
        for i in range(80):
            t = (i / 80) * math.pi * 2
            x = 16 * math.pow(math.sin(t), 3)
            y = -(13 * math.cos(t) - 5 * math.cos(2 * t) - 2 * math.cos(3 * t) - math.cos(4 * t))
            
            points.append({
                "x": cx + x * scale * s,
                "y": cy + y * scale * s,
                "alpha": 0,
                "target": random.uniform(80, 180),
                "delay": random.uniform(0, 8000),
            })

    return points

points = heart_points()

# Asosiy o'yin tsikli (Main Loop)
running = True
start_ticks = pygame.time.get_ticks()

while running:
    current_time = pygame.time.get_ticks() - start_ticks
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(BG)

    # Nuqtalarni chizish va olmosdek miltillash effektini berish
    for p in points:
        if current_time > p["delay"]:
            # Alpha (shaffoflik) darajasini maqsaddagiga qarab silliq oshirish
            if p["alpha"] < p["target"]:
                p["alpha"] += 2
                if p["alpha"] > p["target"]:
                    p["alpha"] = p["target"]

        # Matn va uning shaffofligini sozlash
        text_surface = font.render(TEXT, True, PINK)
        text_surface.set_alpha(int(p["alpha"]))
        
        # Matn markazini nuqtaga joylashtirish
        rect = text_surface.get_rect(center=(int(p["x"]), int(p["y"])))
        screen.blit(text_surface, rect)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()