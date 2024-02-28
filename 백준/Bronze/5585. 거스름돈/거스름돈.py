import sys

coins = (500, 100, 50, 10, 5, 1)
price = int(sys.stdin.readline())
change = 1_000 - price
cnt = 0
for coin in coins:
    if change < coin:
        continue
    if change == 0:
        break
    cnt += change // coin
    change %= coin
print(cnt)
