import sys


def input():
    return sys.stdin.readline().rstrip()


a = int(input())
opr = input()
b = int(input())
print(a * b if opr == '*' else a + b)
