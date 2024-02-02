import sys

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append((int(sys.stdin.readline()), i))
sorted_a = sorted(a)
max_dist = 0
for i in range(n):
    max_dist = max(max_dist, sorted_a[i][1] - a[i][1])
print(max_dist + 1)
