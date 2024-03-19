def solution(arr):
    stack = []
    for n in arr:
        if stack:
            if stack[-1] != n:
                stack.append(n)
        else:
            stack.append(n)
    return stack
