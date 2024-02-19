import sys

prime = [False, False] + [True] * 999_999
for i in range(2, 1_000_001):
    if prime[i]:
        for j in range(i * 2, 1_000_001, i):
            prime[j] = False
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    cnt = 0
    for i in range(2, n // 2 + 1):
        if prime[i] and prime[n - i]:
            cnt += 1
    print(cnt)
