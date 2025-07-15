import sys

n = int(sys.stdin.readline())
participants = []
for i in range(n):
    participants.append(tuple(map(int, sys.stdin.readline().split())))
participants.sort(key = lambda x: [-x[0], x[1]])
cnt = 0
for i in range(n):
    if participants[4][0] == participants[i][0] and participants[4][1] < participants[i][1]:
        cnt += 1
print(cnt)
