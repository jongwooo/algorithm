import sys


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
exp = input()
nums = [int(input()) for _ in range(n)]
stack = []
for e in exp:
    if 'A' <= e <= 'Z':
        stack.append(nums[ord(e) - ord('A')])
    else:
        n2 = stack.pop()
        n1 = stack.pop()
        if e == '+':
            stack.append(n1 + n2)
        elif e == '-':
            stack.append(n1 - n2)
        elif e == '*':
            stack.append(n1 * n2)
        elif e == '/':
            stack.append(n1 / n2)
print(format(stack[0], '.2f'))
