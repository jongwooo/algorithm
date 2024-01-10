n = int(input())
drinks = sorted(map(int, input().split()), reverse=True)
print(drinks[0] + sum(drinks[i] / 2 for i in range(1, n)))
