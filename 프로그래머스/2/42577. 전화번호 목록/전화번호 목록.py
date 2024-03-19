def solution(phone_book):
    hash_map = {}
    for nums in phone_book:
        hash_map[nums] = 1
    for nums in phone_book:
        temp = ''
        for num in nums:
            temp += num
            if temp in hash_map and temp != nums:   
                return False
    return True
