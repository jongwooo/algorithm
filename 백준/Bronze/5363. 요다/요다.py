import sys

n = int(sys.stdin.readline())
for _ in range(n):
    words = sys.stdin.readline().rstrip().split()
    print(*words[2:], *words[:2])
