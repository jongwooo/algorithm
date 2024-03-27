import sys

a, b = map(int, sys.stdin.readline().split())
print(a // b, end='')
if a % b:
    print('.', end='')
    i = 0
    while a % b and i < 1000:
        a = a % b * 10
        i += 1
        print(a // b, end='')
