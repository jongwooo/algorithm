import sys

q = int(sys.stdin.readline())
for _ in range(q):
    a = int(sys.stdin.readline())
    print(1 if (a & (-a)) == a else 0)
