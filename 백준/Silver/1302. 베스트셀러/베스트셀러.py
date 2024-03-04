import sys

n = int(sys.stdin.readline())
rank = dict()
for _ in range(n):
    book = sys.stdin.readline().rstrip()
    if book not in rank:
        rank[book] = 1
    else:
        rank[book] += 1
sorted_rank = sorted(rank.items(), key=lambda x: (-x[1], x[0]))
print(sorted_rank[0][0])
