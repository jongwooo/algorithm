import sys

string = sys.stdin.readline().rstrip()
stack = []
result = 0
temp = 1
for i in range(len(string)):
    if string[i] == '(':
        temp *= 2
        stack.append('(')
    elif string[i] == '[':
        temp *= 3
        stack.append('[')
    elif string[i] == ')':
        if not stack or stack[-1] != '(':
            result = 0
            break
        elif string[i - 1] == '(':
            result += temp
        temp //= 2
        stack.pop()
    elif string[i] == ']':
        if not stack or stack[-1] != '[':
            result = 0
            break
        elif string[i - 1] == '[':
            result += temp
        temp //= 3
        stack.pop()
if stack:
    result = 0
print(result)
