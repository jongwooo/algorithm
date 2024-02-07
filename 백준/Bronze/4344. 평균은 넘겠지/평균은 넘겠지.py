import sys

c = int(sys.stdin.readline())
for _ in range(c):
    data = list(map(int, sys.stdin.readline().split()))
    n = data[0]
    avg = sum(data[1:]) / n
    cnt = 0
    for d in data[1:]:
        if avg < d:
            cnt += 1
    print(f'{cnt / n * 100:.3f}%')
