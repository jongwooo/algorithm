import sys

n, m = map(int, sys.stdin.readline().split())
problem_cnt = 0
for _ in range(n):
    s = list(sys.stdin.readline().rstrip())
    cnt = 0
    for i in s:
        if i == 'O':
            cnt += 1
    if m // 2 + 1 <= cnt:
        problem_cnt += 1
print(problem_cnt)
