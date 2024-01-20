dp = [0, 1, 2, 4]
for i in range(4, 11):
    dp.append(sum(dp[i - 3:i]))
t = int(input())
for _ in range(t):
    n = int(input())
    print(dp[n])
