import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    one = []
    idx = 0
    while n > 0:
        if n % 2 == 1:
            one.append(idx)
        n //= 2
        idx += 1
    print(*one)
    