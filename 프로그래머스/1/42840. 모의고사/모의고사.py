def solution(answers):
    one = (1, 2, 3, 4, 5)
    two = (2, 1, 2, 3, 2, 4, 2, 5)
    three = (3, 3, 1, 1, 2, 2, 4, 4, 5, 5)
    corrects = [0, 0, 0]
    for i, answer in enumerate(answers):
        if answer == one[(i + 5) % 5]:
            corrects[0] += 1
        if answer == two[(i + 8) % 8]:
            corrects[1] += 1
        if answer == three[(i + 10) % 10]:
            corrects[2] += 1
    max_score = max(corrects)
    result = []
    for i in range(3):
        if corrects[i] == max_score:
            result.append(i + 1)
    return result
