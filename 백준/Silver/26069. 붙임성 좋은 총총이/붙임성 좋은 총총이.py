import sys

n = int(sys.stdin.readline())
visited = set()
visited.add('ChongChong')
for _ in range(n):
    a, b = sys.stdin.readline().rstrip().split()
    if a in visited and b not in visited:
        visited.add(b)
    elif b in visited and a not in visited:
        visited.add(a)
print(len(visited))
