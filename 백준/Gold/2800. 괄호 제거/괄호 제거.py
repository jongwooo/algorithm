import sys


def input():
    return sys.stdin.readline().rstrip()


def combination(start, length):
    for i in range(start, length):
        first, end = bracket_pair[i]
        exp[first] = ''
        exp[end] = ''
        result.add(''.join(exp))
        combination(i + 1, length)
        exp[first] = '('
        exp[end] = ')'


exp = list(input())
stack = []
bracket_pair = []
result = set()
for i in range(len(exp)):
    if exp[i] == '(':
        stack.append(i)
    elif exp[i] == ')':
        first = stack.pop()
        bracket_pair.append((first, i))
combination(0, len(bracket_pair))
for r in sorted(list(result)):
    print(r)
