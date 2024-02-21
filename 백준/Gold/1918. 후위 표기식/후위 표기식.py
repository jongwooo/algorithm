import sys

exp = sys.stdin.readline().rstrip()
stack = []
result = []
for x in exp:
    if x.isalpha():
        result.append(x)
    elif x == '(':
        stack.append(x)
    elif x == '*' or x == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            result.append(stack.pop())
        stack.append(x)
    elif x == '+' or x == '-':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.append(x)
    elif x == ')':
        while stack and stack[-1] != '(':
            result.append(stack.pop())
        stack.pop()
while stack:
    result.append(stack.pop())
print(''.join(result))
