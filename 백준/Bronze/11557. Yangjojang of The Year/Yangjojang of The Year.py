import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    dic = dict()
    for _ in range(n):
        s, liter = sys.stdin.readline().split()
        dic[s] = int(liter)
    print(max(dic, key=dic.get))
