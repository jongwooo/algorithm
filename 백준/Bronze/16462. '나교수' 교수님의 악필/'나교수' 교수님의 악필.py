import sys
import math

n = int(sys.stdin.readline())
total_score = 0
for _ in range(n):
    score = sys.stdin.readline().rstrip()
    formatted_score = ''
    for number in score:
        if number in ('0', '6', '9'):
            formatted_score += '9'
        else:
            formatted_score += number
    if 100 < int(formatted_score):
        formatted_score = 100
    else:
        formatted_score = int(formatted_score)
    total_score += formatted_score
average_score = total_score / n
if average_score - int(average_score) < 0.5:
    print(math.floor(average_score))
else:
    print(math.ceil(average_score))
