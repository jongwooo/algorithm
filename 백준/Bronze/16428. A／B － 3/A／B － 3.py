import sys

a, b = map(int, sys.stdin.readline().split())
q, r = divmod(a, b)
if a != 0 and r < 0:
    q, r = q + 1, r - b
print(q)
print(r)
