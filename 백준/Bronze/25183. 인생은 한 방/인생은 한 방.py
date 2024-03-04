import sys

n = int(sys.stdin.readline())
s = list(sys.stdin.readline().rstrip())
max_cnt = 0
cnt = 1
for i in range(1, n):
    if abs(ord(s[i - 1]) - ord(s[i])) == 1:
        cnt += 1
    else:
        max_cnt = max(max_cnt, cnt)
        cnt = 1
max_cnt = max(max_cnt, cnt)
print('YES' if max_cnt >= 5 else 'NO')
