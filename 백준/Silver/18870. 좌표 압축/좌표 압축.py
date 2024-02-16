import sys

n = int(sys.stdin.readline())
x = list(map(int, sys.stdin.readline().split()))
sorted_x = sorted(list(set(x)))
dic = dict(zip(sorted_x, range(len(sorted_x))))
for xi in x:
    print(dic[xi], end=' ')
