import sys

n = int(sys.stdin.readline())
office = {}
for _ in range(n):
    name, log = map(str, input().split())
    if log == 'enter':
        office[name] = True
    else:
        del office[name]
names = sorted(office, reverse=True)
for name in names:
    print(name)
