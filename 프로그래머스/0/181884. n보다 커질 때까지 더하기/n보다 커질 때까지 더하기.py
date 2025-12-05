def solution(numbers, n):
    num_sum = 0
    for i in range(len(numbers)):
        num_sum += numbers[i]
        if n < num_sum:
            break
    return num_sum
