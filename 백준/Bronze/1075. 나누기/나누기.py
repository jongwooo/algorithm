import sys

n = int(sys.stdin.readline())
f = int(sys.stdin.readline())
result = (n // 100) * 100
while result % f != 0:
    result += 1
print(str(result)[-2:])
