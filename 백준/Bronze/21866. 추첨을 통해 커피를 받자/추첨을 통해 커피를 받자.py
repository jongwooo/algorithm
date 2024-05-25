import sys

max_scores = (100, 100, 200, 200, 300, 300, 400, 400, 500)
scores = list(map(int, sys.stdin.readline().split()))
total_score, hacker = 0, 0
for i in range(9):
    if scores[i] > max_scores[i]:
        hacker = 1
    total_score += scores[i]
if hacker:
    print('hacker')
else:
    print('draw' if total_score >= 100 else 'none')
