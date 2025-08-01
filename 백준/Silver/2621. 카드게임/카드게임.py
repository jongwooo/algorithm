import sys

card = []
colors = []
numbers = []
for _ in range(5):
    c, n = sys.stdin.readline().split()
    n = int(n)
    card.append((c, n))
    colors.append(c)
    numbers.append(n)
cnt_color = {'R': 0, 'B': 0, 'Y': 0, 'G': 0}
cnt_num = [0 for _ in range(11)]
for i in range(5):
    color, number = card[i]
    cnt_color[color] += 1
    cnt_num[number] += 1
sort_nums = sorted(numbers.copy())
if 5 in cnt_color.values() and sort_nums[0] + 1 == sort_nums[1] and sort_nums[1] + 1 == sort_nums[2] and sort_nums[
    2] + 1 == sort_nums[3] and sort_nums[3] + 1 == sort_nums[4]:
    score = max(numbers) + 900
elif 4 in cnt_num:
    score = cnt_num.index(4) + 800
elif 3 in cnt_num and 2 in cnt_num:
    score = cnt_num.index(3) * 10 + cnt_num.index(2) + 700
elif 5 in cnt_color.values():
    score = max(numbers) + 600
elif sort_nums[0] + 1 == sort_nums[1] and sort_nums[1] + 1 == sort_nums[2] and sort_nums[2] + 1 == sort_nums[3] and \
        sort_nums[3] + 1 == sort_nums[4]:
    score = max(numbers) + 500
elif 3 in cnt_num:
    score = cnt_num.index(3) + 400
elif 2 in cnt_num:
    first = cnt_num.index(2)
    num1 = numbers.copy()
    for i in num1:
        if i == first:
            numbers.remove(i)
    cnt_num[first] = 0
    if 2 in cnt_num:
        second = cnt_num.index(2)
        score = max(first, second) * 10 + min(first, second) + 300
    else:
        score = first + 200
else:
    score = max(numbers) + 100
print(score)
