import heapq


def solution(operations):
    answer = []
    numbers = []
    for operation in operations:
        alphabet, number = operation.split()
        number = int(number)
        if alphabet == 'I':
            heapq.heappush(numbers, number)    
        else:
            if numbers:
                if number == -1:
                    heapq.heappop(numbers)
                else:
                    numbers.sort()
                    numbers.pop()
    if numbers:
        numbers.sort()
        return [numbers[-1], numbers[0]]
    return [0, 0]
