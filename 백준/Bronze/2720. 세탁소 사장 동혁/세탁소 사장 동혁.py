import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    coins = {25: 0, 10: 0, 5: 0, 1: 0}
    c = int(input())
    for coin in coins.keys():
        coins[coin] = c // coin
        c %= coin
    for cnt in coins.values():
        print(cnt, end=' ')
    print()
