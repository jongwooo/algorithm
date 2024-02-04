import sys

while True:
    string = sys.stdin.readline().rstrip()
    stack = []
    if string == '.':
        break
    for s in string:
        if s == '(' or s == '[':
            stack.append(s)
        elif s == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                stack.append('(')
                break
        elif s == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                stack.append('[')
                break
    print('yes' if not stack else 'no')
