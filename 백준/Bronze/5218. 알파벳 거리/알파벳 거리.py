import sys

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = sys.stdin.readline().rstrip().split()
    result = []
    for i in range(len(a)):
        if ord(a[i]) > ord(b[i]):
            result.append(26 - (ord(a[i]) - ord(b[i])))
        else:
            result.append(abs(ord(b[i]) - ord(a[i])))
    print('Distances:', *result)
