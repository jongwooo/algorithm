import sys

price = int(sys.stdin.readline())
for _ in range(9):
    price -= int(sys.stdin.readline())
print(price)
