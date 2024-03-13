import sys

scores = sorted([(i, int(sys.stdin.readline())) for i in range(1, 9)], key=lambda x: -x[1])[:5]
score_sum = 0
temp = []
for i, score in scores:
    score_sum += score
    temp.append(i)
temp.sort()
print(score_sum)
print(*temp)
