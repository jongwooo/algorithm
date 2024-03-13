import sys

r, g, b = map(int, sys.stdin.readline().split())
min_ball = min(r, g, b)
result = min_ball
r -= min_ball
g -= min_ball
b -= min_ball
result += r // 3 + g // 3 + b // 3
r %= 3
g %= 3
b %= 3
if r == 2:
    result += 1
    r = 0
if g == 2:
    result += 1
    g = 0
if b == 2:
    result += 1
    b = 0
if r + g + b > 0:
    result += 1
print(result)
