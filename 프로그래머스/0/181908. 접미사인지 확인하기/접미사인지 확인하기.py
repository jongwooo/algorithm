def solution(my_string, is_suffix):
    for i in range(len(my_string)):
        if my_string[len(my_string) - i - 1:] == is_suffix:
            return 1
    return 0
