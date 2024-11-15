import sys

n, m = map(int, sys.stdin.readline().split())
buckets = [i for i in range(1, n + 1)]
for _ in range(m):
    i, j, k = map(int, sys.stdin.readline().split())
    buckets = buckets[:i - 1] + buckets[k - 1:j] + buckets[i - 1:k - 1] + buckets[j:]
print(*buckets)
