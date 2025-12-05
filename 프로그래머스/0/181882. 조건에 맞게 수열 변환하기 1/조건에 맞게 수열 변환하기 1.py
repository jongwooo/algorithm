def solution(arr):
    result = []
    for i in range(len(arr)):
        x = arr[i]
        if arr[i] >= 50 and arr[i] % 2 == 0:
            result.append(arr[i] / 2)
        elif arr[i] < 50 and arr[i] % 2 == 1:
            result.append(arr[i] * 2)
        else:
            result.append(arr[i])
    return result
