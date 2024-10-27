import sys

n = int(sys.stdin.readline())
for _ in range(n):
    l, d = sys.stdin.readline().split('-')
    value = 0
    for i in range(3):
        value += ((ord(l[i]) - 65) * 26 ** (2 - i))
    print('nice' if abs(value - int(d)) <= 100 else 'not nice')
