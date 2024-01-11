string = input()
max_num, min_num = '', ''
cnt = 0
for s in string:
    if s == 'M':
        cnt += 1
    else:
        if cnt > 0:
            max_num += str(5 * 10 ** cnt)
            min_num += str(10 ** cnt + 5)
        else:
            max_num += '5'
            min_num += '5'
        cnt = 0
if cnt != 0:
    max_num += '1' * cnt
    min_num += str(10 ** (cnt - 1))
print(f'{max_num}\n{min_num}')
