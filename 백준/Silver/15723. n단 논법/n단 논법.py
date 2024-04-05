import sys

n = int(sys.stdin.readline())
graph = [[False] * 26 for _ in range(26)]
for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split(' is ')
    graph[ord(a) - 97][ord(b) - 97] = True
for k in range(26):
    for a in range(26):
        for b in range(26):
            if a == b:
                continue
            if graph[a][k] and graph[k][b]:
                graph[a][b] = True
m = int(sys.stdin.readline())
for _ in range(m):
    a, b = sys.stdin.readline().rstrip().split(' is ')
    print('T' if graph[ord(a) - 97][ord(b) - 97] else 'F')
