import sys


def input():
    return sys.stdin.readline().rstrip()


n, k = map(int, input().split())
peoples = [(i + 1) for i in range(n)]
evicted = []
idx = k - 1
while peoples:
    idx %= len(peoples)
    evicted.append(peoples.pop(idx))
    idx += k - 1
print(f'<{", ".join(map(str, evicted))}>')
