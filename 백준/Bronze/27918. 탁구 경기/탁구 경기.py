import sys

n = int(sys.stdin.readline())
x, y = 0, 0
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if s == 'D':
        x += 1
    else:
        y += 1
    if abs(x - y) > 1:
        break
print(f'{x}:{y}')
