import sys

n = int(sys.stdin.readline())
result = 0
for _ in range(n):
    w, h = map(int, sys.stdin.readline().split())
    if w == 136:
        result += 1_000
    elif w == 142:
        result += 5_000
    elif w == 148:
        result += 10_000
    elif w == 154:
        result += 50_000
print(result)
