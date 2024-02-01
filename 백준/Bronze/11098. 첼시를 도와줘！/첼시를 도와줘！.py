import sys

n = int(sys.stdin.readline())
for _ in range(n):
    p = int(sys.stdin.readline())
    dic = dict()
    for _ in range(p):
        c, name = sys.stdin.readline().split()
        dic[name] = int(c)
    print(max(dic, key=dic.get))
