import sys
import math

h, w, n, m = list(map(int, sys.stdin.readline().split()))
a = math.ceil(h / (n + 1))
b = math.ceil(w / (m + 1))
print(a * b)
