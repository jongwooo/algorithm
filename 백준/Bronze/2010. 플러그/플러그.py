import sys

n = int(sys.stdin.readline())
result = 0
for _ in range(n):
    result += int(sys.stdin.readline())
print(result - n + 1)
