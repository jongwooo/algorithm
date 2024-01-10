n = int(input())
prices = sorted([int(input()) for _ in range(n)], reverse=True)
print(sum(prices[i] for i in range(n) if (i + 1) % 3 != 0))
