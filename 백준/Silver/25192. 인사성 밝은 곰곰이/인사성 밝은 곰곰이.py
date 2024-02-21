import sys

n = int(sys.stdin.readline())
emoji = set()
cnt = 0
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if s != 'ENTER':
        if s not in emoji:
            emoji.add(s)
            cnt += 1
    elif s == 'ENTER':
        emoji.clear()
print(cnt)
