n = int(input())
tips = sorted([int(input()) for i in range(n)], reverse=True)
print(sum(tips[i] - i for i in range(n) if tips[i] - i > 0))
