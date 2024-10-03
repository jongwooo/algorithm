import sys

a, b = map(int, sys.stdin.readline().split())
c, d = map(int, sys.stdin.readline().split())
table = [a / c + b / d, c / d + a / b, d / b + c / a, b / a + d / c]
print(table.index(max(table)))
