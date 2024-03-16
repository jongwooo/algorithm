import sys

n = int(sys.stdin.readline())
candidates = []
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    if len(name) == 3:
        candidates.append(name)
candidates.sort()
print(candidates[0])
