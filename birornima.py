# import random
# import time
# import os

# os.system('cls' if os.name == 'nt' else 'clear')
# chars = "abcdefghijklmnopqrstuvwxyz0123456789@#$%^&*()"
# width = 80

# try:
#     while True:
#         line = "".join(random.choice(chars) if random.random() > 0.7 else " " for _ in range(width))
#         print(f"\033[92m{line}\033[0m")
#         time.sleep(0.05)
# except KeyboardInterrupt:
#     print("\nMatrix to'xtatildi.")

import datetime

now = datetime.datetime.now()
start_of_year = datetime.datetime(now.year, 1, 1)
end_of_year = datetime.datetime(now.year + 1, 1, 1)

total_seconds = (end_of_year - start_of_year).total_seconds()
passed_seconds = (now - start_of_year).total_seconds()

percentage = (passed_seconds / total_seconds) * 100
bar_length = 30
filled = int(bar_length * percentage // 100)
bar = "█" * filled + "░" * (bar_length - filled)

print(f"\n🗓️  {now.year}-yil progressi: [{bar}] {percentage:.2f}%\n")