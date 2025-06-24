import sys

na, nb = map(int, sys.stdin.readline().split())
a = set(map(int, sys.stdin.readline().split()))
b = set(map(int, sys.stdin.readline().split()))
result = sorted(list(a - b))
if result:
    print(len(result))
    print(*result)
else:
    print(0)
