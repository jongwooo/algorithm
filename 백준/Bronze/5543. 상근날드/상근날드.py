import sys

hamburger = []
drink = []
for _ in range(3):
    hamburger.append(int(sys.stdin.readline()))
for _ in range(2):
    drink.append(int(sys.stdin.readline()))
print(min(hamburger) + min(drink) - 50)
