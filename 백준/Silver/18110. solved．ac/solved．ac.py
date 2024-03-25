import sys


def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)


n = int(sys.stdin.readline())
if not n:
    print(0)
else:
    difficulty = sorted([int(sys.stdin.readline()) for _ in range(n)])
    exception = my_round(n * 0.15)
    if exception != 0:
        difficulty = difficulty[exception: -exception]
    cnt = n - 2 * exception
    result = sum(difficulty)
    print(my_round(result / cnt))
