import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    print(f'{n} is {"odd" if n % 2 else "even"}')
