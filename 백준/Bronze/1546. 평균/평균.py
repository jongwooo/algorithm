n = int(input())
score = sorted(list(map(float, input().split())))
max_score = score[-1]
for i in range(n):
    score[i] = score[i] / max_score * 100
print(sum(score) / n)
