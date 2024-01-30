import sys


n = int(sys.stdin.readline())
max_reward = 0
for _ in range(n):
    a, b, c = sorted(map(int, sys.stdin.readline().split()))
    reward = 0
    if a == b == c:
        reward = 10000 + a * 1000
    elif a == b or b == c:
        reward = 1000 + b * 100
    else:
        reward = c * 100
    max_reward = max(max_reward, reward)
print(max_reward)
