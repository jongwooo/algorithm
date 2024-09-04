import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for _ in range(n)]
m = int(sys.stdin.readline())
price = 0
for _ in range(m):
    b = int(sys.stdin.readline()) - 1
    price += a[b]
print(price)
