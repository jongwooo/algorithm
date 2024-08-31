import sys

n = int(sys.stdin.readline())
result = 6
for i in range(11, n + 1):
    result *= i
print(result)
