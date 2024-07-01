import sys

n = int(sys.stdin.readline())
candidate = [0] * 3
squared = [0] * 3
for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().split())
    candidate[0] += a
    candidate[1] += b
    candidate[2] += c
    squared[0] += a ** 2
    squared[1] += b ** 2
    squared[2] += c ** 2
m = max(candidate)
if candidate.count(m) == 1:
    for i in range(len(candidate)):
        if candidate[i] == m:
            print(i + 1, m)
            break
else:
    pow_m = max(squared)
    elected = 0
    for i in range(len(squared)):
        if squared[i] == pow_m:
            elected = i
            break
    if squared.count(pow_m) > 1:
        print(0, candidate[elected])
    else:
        print(elected + 1, candidate[elected])
