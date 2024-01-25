import sys


def input():
    return sys.stdin.readline()


t = int(input())
for _ in range(t):
    expressions = input().split()
    number = float(expressions[0])
    for i in range(1, len(expressions)):
        if expressions[i] == '@':
            number *= 3
        elif expressions[i] == '%':
            number += 5
        elif expressions[i] == '#':
            number -= 7
    print(format(number, '.2f'))
