import math
import sys

x1, y1, r1 = map(int, sys.stdin.readline().split())
x2, y2, r2 = map(int, sys.stdin.readline().split())
d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print('YES' if r1 + r2 > d else 'NO')
