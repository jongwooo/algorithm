import sys

n = int(sys.stdin.readline())
quotation_cnt = sorted(list(map(int, sys.stdin.readline().split())))
for k in range(n, -1, -1):
    if k <= quotation_cnt[-k]:
        print(k)
        break
