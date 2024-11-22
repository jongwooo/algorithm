import sys

n, m, k = map(int, sys.stdin.readline().split())
score = []
for i in range(n):
    sub1, sub2 = map(int, sys.stdin.readline().split())
    if sub2 <= m:
        score.append(140)
    elif sub1 <= m:
        score.append(100)
score = sorted(score, reverse=True)
print(sum(score[:k]))
