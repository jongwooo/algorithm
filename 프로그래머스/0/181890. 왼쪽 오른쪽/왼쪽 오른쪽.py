def solution(str_list):
    result = []
    for i in range(len(str_list)):
        if str_list[i] == 'l':
            result = str_list[:i]
            break
        if str_list[i] == 'r':
            result = str_list[i + 1:]
            break
    return result
