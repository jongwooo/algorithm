import sys

first = len(sys.stdin.readline())
second = len(sys.stdin.readline())
print('no' if first < second else 'go')
