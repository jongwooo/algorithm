import sys

k = int(sys.stdin.readline())
for x in range(1, k + 1):
    data = list(map(int, sys.stdin.readline().split()))
    scores = sorted(data[1:])
    max_diff = 0
    for i in range(data[0] - 1):
        max_diff = max(max_diff, scores[i + 1] - scores[i])
    print(f'Class {x}\nMax {scores[-1]}, Min {scores[0]}, Largest gap {max_diff}')
