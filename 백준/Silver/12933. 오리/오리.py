sound = list(input())
quack = 'quack'
visited = [False] * len(sound)
cnt = [0] * len(sound)
valid = True
for i in range(len(sound)):
    if sound[i] != quack[0]:
        continue
    j, idx = i, 0
    while idx < 5 and j < len(sound):
        if not visited[j] and sound[j] == quack[idx]:
            visited[j] = True
            idx += 1
        j += 1
    if idx != 5:
        valid = False
    for k in range(i, j):
        cnt[k] += 1
ans = 0
for i in range(len(sound)):
    ans = max(ans, cnt[i])
    if cnt[i] == 0:
        valid = False
if valid:
    print(ans)
else:
    print(-1)
