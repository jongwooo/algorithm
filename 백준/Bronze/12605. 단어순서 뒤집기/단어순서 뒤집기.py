import sys

n = int(sys.stdin.readline())
for tc in range(1, n + 1):
    words = sys.stdin.readline().rstrip().split()
    print(f'Case #{tc}: {" ".join(words[::-1])}')
