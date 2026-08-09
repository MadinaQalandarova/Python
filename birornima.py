import random
import time
import os

os.system('cls' if os.name == 'nt' else 'clear')
chars = "abcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()"
width = 80

try:
    while True:
        line = "".join(random.choice(chars) if random.random() > 0.7 else " " for _ in range(width))
        print(f"\033[92m{line}\033[0m")
        time.sleep(0.05)
except KeyboardInterrupt:
    print("\nMatrix to'xtatildi.")