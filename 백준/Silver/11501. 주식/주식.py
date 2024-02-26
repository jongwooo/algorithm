import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))
    money = 0
    max_price = 0
    for i in range(n - 1, -1, -1):
        if max_price < prices[i]:
            max_price = prices[i]
        else:
            money += max_price - prices[i]
    print(money)
