def solution(clothes):
    clothes_dict = {}
    for _, cloth_type in clothes:
        if cloth_type not in clothes_dict:
            clothes_dict[cloth_type] = 1
        else:
            clothes_dict[cloth_type] += 1
    result = 1
    for v in clothes_dict.values():
        result *= v + 1
    return result - 1
