def dfs(numbers, target, depth):
    cnt = 0
    if depth == len(numbers):
        return 1 if sum(numbers) == target else 0
    else:
        cnt += dfs(numbers, target, depth + 1)
        numbers[depth] *= -1
        cnt += dfs(numbers, target, depth + 1)
        return cnt
    

def solution(numbers, target):
    return dfs(numbers, target, 0)
    