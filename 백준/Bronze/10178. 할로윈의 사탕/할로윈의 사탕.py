import sys

t = int(sys.stdin.readline())
for _ in range(t):
    c, v = map(int, sys.stdin.readline().split())
    print(f'You get {c // v} piece(s) and your dad gets {c % v} piece(s).')
