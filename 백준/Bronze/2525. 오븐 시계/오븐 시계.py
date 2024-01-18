h, m = map(int, input().split())
t = int(input())
m += t % 60
h += t // 60
if m >= 60:
    m -= 60
    h += 1
h %= 24
print(h, m)
