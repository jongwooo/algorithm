def solution(progresses, speeds):
    answer = []
    stack = []
    duration = []
    for p, s in zip(progresses, speeds):
        duration.append((100 - p) // s + ((100 - p) % s > 0))
    for d in duration:
        if not stack:
            stack.append(d)
        else:
            if stack[0] < d:
                answer.append(len(stack))
                stack.clear()
            stack.append(d)
    if stack:
        answer.append(len(stack))
    return answer
