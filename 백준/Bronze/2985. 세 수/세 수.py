import sys

a, b, c = map(int, sys.stdin.readline().split())
if a + b == c:
    print(f'{a}+{b}={c}')
elif a - b == c:
    print(f'{a}-{b}={c}')
elif a * b == c:
    print(f'{a}*{b}={c}')
elif a // b == c:
    print(f'{a}/{b}={c}')
elif a == b + c:
    print(f'{a}={b}+{c}')
elif a == b - c:
    print(f'{a}={b}-{c}')
elif a == b * c:
    print(f'{a}={b}*{c}')
elif a == b // c:
    print(f'{a}={b}/{c}')
