import sys

t = int(sys.stdin.readline())
for tc in range(1, t + 1):
    print(f'Case {tc}: {sum(map(int, sys.stdin.readline().split()))}')
