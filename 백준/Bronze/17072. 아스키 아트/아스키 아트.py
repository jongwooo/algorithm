import sys


def intensity(tmp):
    i = (2126 * tmp[0]) + (7152 * tmp[1]) + (722 * tmp[2])
    if 0 <= i < 510_000:
        return '#'
    elif 510_000 <= i < 1_020_000:
        return 'o'
    elif 1_020_000 <= i < 1_530_000:
        return '+'
    elif 1_530_000 <= i < 2_040_000:
        return '-'
    elif i >= 2_040_000:
        return '.'


n, m = map(int, sys.stdin.readline().split())
ascii_list = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
col = []
cnt = 0
result = []
temp = []
for i in ascii_list:
    col = []
    for j in i:
        temp.append(j)
        cnt += 1
        if cnt == 3:
            col.append(intensity(temp))
            temp = []
            cnt = 0
    result.append(col)
for i in result:
    for j in i:
        print(j, end='')
    print()
