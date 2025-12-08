def solution(num_list):
    if len(num_list) >= 11:
        return sum(num_list)
    result = 1
    for n in num_list:
        result *= n
    return result
