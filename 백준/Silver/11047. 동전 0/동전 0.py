n, k = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse=True)
cnt = 0
for coin in coins:
    if k >= coin:
        q, k = divmod(k, coin)
        cnt += q
print(cnt)
