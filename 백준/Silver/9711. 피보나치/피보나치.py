import sys

t = int(sys.stdin.readline())
for tc in range(1, t + 1):
    p, q = map(int, sys.stdin.readline().split())
    if (p == 1 or p == 2) and q == 1:
        print(f'Case #{tc}: 0')
    else:
        dp = [0, 1]
        for i in range(2, p + 1):
            dp.append((dp[i - 1] + dp[i - 2]) % q)
        print(f'Case #{tc}: {dp[p]}')
