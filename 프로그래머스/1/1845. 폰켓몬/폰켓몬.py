def solution(nums):
    num_len = len(set(nums))
    result = len(nums) // 2
    return result if result < num_len else num_len
