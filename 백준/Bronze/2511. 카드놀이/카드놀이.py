import sys

a = list(map(int, sys.stdin.readline().split()))
b = list(map(int, sys.stdin.readline().split()))
a_cnt, b_cnt = 0, 0
for i in range(10):
    if a[i] > b[i]:
        a_cnt += 3
    elif a[i] < b[i]:
        b_cnt += 3
    else:
        a_cnt += 1
        b_cnt += 1
print(a_cnt, b_cnt)
if a_cnt > b_cnt:
    print('A')
elif a_cnt < b_cnt:
    print('B')
elif a_cnt == b_cnt == 10:
    print('D')
else:
    for i in range(1, 11):
        if a[-i] > b[-i]:
            print('A')
            break
        elif a[-i] < b[-i]:
            print('B')
            break
        else:
            continue