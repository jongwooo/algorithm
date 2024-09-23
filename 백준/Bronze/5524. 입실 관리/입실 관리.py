import sys

n = int(sys.stdin.readline())
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    print(name.lower())
