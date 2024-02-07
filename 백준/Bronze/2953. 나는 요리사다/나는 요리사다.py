import sys

max_point = 0
winner = 0
for player in range(1, 6):
    point = sum(list(map(int, sys.stdin.readline().split())))
    if max_point < point:
        max_point = point
        winner = player
print(winner, max_point)
