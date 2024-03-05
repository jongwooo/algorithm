import sys

t = int(sys.stdin.readline())
for i in range(1, t + 1):
    a, b, c = sorted(map(int, sys.stdin.readline().split()), reverse=True)
    if a >= b + c:
        print(f'Case #{i}: invalid!')
    elif a == b == c:
        print(f'Case #{i}: equilateral')
    elif a == b or b == c:
        print(f'Case #{i}: isosceles')
    else:
        print(f'Case #{i}: scalene')
