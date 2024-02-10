import sys

names = sys.stdin.readline().split('-')
for name in names:
    print(name[0], end='')
