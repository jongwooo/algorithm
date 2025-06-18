import sys


def lucas(n, k):
    if n < k:
        return 0
    if n == k:
        return 1
    x = 1
    for i in range(1, k + 1):
        x *= n - i  + 1
        x //= i
    return x


N, K, M = map(int, sys.stdin.readline().split())
n_list, m_list = [], []
cnt = 0
while N or K:
    n_list.append(N % M)
    m_list.append(K % M)
    N //= M
    K //= M
result = 1
for i in range(len(n_list)):
    result *= lucas(n_list[i], m_list[i])
    result %= M
print(result)
