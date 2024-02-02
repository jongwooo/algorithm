import math
import sys

n, w, h = map(int, sys.stdin.readline().split())
t = math.sqrt(w ** 2 + h ** 2)
for _ in range(n):
    print('DA' if int(sys.stdin.readline()) <= t else 'NE')
