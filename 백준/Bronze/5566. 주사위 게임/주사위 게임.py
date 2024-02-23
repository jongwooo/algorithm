import sys

n, m = map(int, sys.stdin.readline().split())
cmd = [0] + [int(sys.stdin.readline()) for _ in range(n)]
dice = [int(sys.stdin.readline()) for _ in range(m)]
player = 1
cnt = 0
for d in dice:
    cnt += 1
    player += d
    if n <= player:
        break
    player += cmd[player]
    if n <= player:
        break
print(cnt)
