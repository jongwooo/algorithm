import sys

sys.setrecursionlimit(10 ** 6)


def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


n = int(sys.stdin.readline())
trees = sorted([int(sys.stdin.readline()) for _ in range(n)])
gaps = []
for i in range(1, len(trees)):
    gaps.append(trees[i] - trees[i - 1])
g = gaps[0]
for j in range(1, len(gaps)):
    g = gcd(g, gaps[j])
result = 0
for each in gaps:
    result += each // g - 1
print(result)
