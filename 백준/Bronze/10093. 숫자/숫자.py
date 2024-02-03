import sys

a, b = map(int, sys.stdin.readline().split())
if a > b:
    print(a - b - 1)
    for x in range(b + 1, a):
        print(x, end=' ')
elif a < b:
    print(b - a - 1)
    for x in range(a + 1, b):
        print(x, end=' ')
else:
    print(a - b)
