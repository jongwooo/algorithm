import sys

n, k = map(int, sys.stdin.readline().split())
cnt = 0
for h in range(n + 1):
    if str(k) in (str(h) if h > 10 else '0' + str(h)):
        cnt += 3600
        continue
    for m in range(60):
        if str(k) in (str(m) if m > 10 else '0' + str(m)):
            cnt += 60
            continue
        for s in range(60):
            if str(k) in (str(s) if s > 10 else '0' + str(s)):
                cnt += 1
print(cnt)
