import sys


def festival1(score):
    if score == 1:
        return 5_000_000
    elif 1 < score <= 3:
        return 3_000_000
    elif 3 < score <= 6:
        return 2_000_000
    elif 6 < score <= 10:
        return 500_000
    elif 10 < score <= 15:
        return 300_000
    elif 15 < score <= 21:
        return 100_000
    else:
        return 0


def festival2(score):
    if score == 1:
        return 5_120_000
    elif 1 < score <= 3:
        return 2_560_000
    elif 3 < score <= 7:
        return 1_280_000
    elif 7 < score <= 15:
        return 640_000
    elif 15 < score <= 31:
        return 320_000
    else:
        return 0


t = int(sys.stdin.readline())
for _ in range(t):
    first, second = map(int, sys.stdin.readline().split())
    print(festival1(first) + festival2(second))
