import sys


def bfs(start, cnt):
    to_go = []
    for line_num in station[start]:
        for a in line[line_num]:
            if a == dest:
                return cnt
            if a not in visited:
                if len(station[a]) > 1:
                    to_go.append(a)
                visited.append(a)
    for x in to_go:
        return bfs(x, cnt + 1)


N = int(sys.stdin.readline())
line = dict()
station = dict()
for line_number in range(1, N + 1):
    temp = list(map(int, sys.stdin.readline().split()))
    line[line_number] = temp[1:]
    for a in temp[1:]:
        if a in station:
            station[a].append(line_number)
        else:
            station[a] = [line_number]
dest = int(sys.stdin.readline())
visited = [0]
cnt = bfs(0, 0)
print(cnt if cnt is not None else -1)
