import sys

n, x = map(int, sys.stdin.readline().split())
socks = list(map(int, sys.stdin.readline().split()))
price = []
for i in range(n - 1):
    price.append((socks[i] + socks[i + 1]) * x)
print(min(price))
