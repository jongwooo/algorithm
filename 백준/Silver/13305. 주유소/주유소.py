n = int(input())
distances = list(map(int, input().split()))
prices = list(map(int, input().split()))
min_price = prices[0]
cost = 0
for i in range(n - 1):
    if prices[i] < min_price:
        min_price = prices[i]
    cost += distances[i] * min_price
print(cost)
