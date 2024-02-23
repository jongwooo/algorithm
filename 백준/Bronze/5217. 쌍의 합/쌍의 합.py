import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    start = 1
    print(f'Pairs for {n}:', end=' ')
    for k in range((n - 1) // 2):
        if k != 0:
            print(',', end=' ')
        print(start, n - start, end='')
        start += 1
    print()
