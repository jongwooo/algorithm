import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(lambda x: int(x, 2), sys.stdin.readline().split())
    print(bin(a + b)[2:])
