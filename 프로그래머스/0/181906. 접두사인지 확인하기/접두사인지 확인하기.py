def solution(my_string, is_prefix):
    for i in range(len(my_string)):
        if my_string[:len(my_string) - i] == is_prefix:
            return 1
    return 0
