import sys

n = int(sys.stdin.readline())
s = list(map(int, sys.stdin.readline().split()))
left = 0
fruit_cnt = {}
max_len = 0
for right in range(n):
    cur_fruit = s[right]
    if cur_fruit in fruit_cnt:
        fruit_cnt[cur_fruit] += 1
    else:
        fruit_cnt[cur_fruit] = 1
    while len(fruit_cnt) > 2:
        fruit_to_remove = s[left]
        fruit_cnt[fruit_to_remove] -= 1
        if fruit_cnt[fruit_to_remove] == 0:
            del fruit_cnt[fruit_to_remove]
        left += 1
    max_len = max(max_len, right - left + 1)
print(max_len)
