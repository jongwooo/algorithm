def solution(my_string):
    result = [0] * 52
    for x in my_string:
        if x.isupper():
            result[ord(x) - 65] += 1
        else:
            result[ord(x) - 71] += 1
    return result
