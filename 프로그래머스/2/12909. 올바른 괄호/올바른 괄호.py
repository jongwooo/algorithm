def solution(brackets):
    if brackets[0] == ')' or brackets[-1] == '(':
        return False
    stack = []
    for bracket in brackets:
        if bracket == '(':
            stack.append(bracket)
        elif stack and bracket == ')':
            stack.pop()
        else:
            return False
    if stack:
        return False
    else:
        return True
