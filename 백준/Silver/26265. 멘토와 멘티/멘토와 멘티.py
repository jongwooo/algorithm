import sys

n = int(sys.stdin.readline())
pair = sorted(sorted([list(sys.stdin.readline().rstrip().split()) for _ in range(n)], key=lambda x: x[1], reverse=True),
              key=lambda x: x[0])
for p in pair:
    print(*p)
