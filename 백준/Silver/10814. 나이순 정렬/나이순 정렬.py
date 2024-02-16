import sys

n = int(sys.stdin.readline())
data = []
for _ in range(n):
    age, name = sys.stdin.readline().split()
    data.append((int(age), name))
data.sort(key=lambda x: x[0])
for d in data:
    print(*d)
