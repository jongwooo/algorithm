a, b, c, = map(int, input().split())
d = int(input())
h = d // 3600
m = (d % 3600) // 60
s = d - h * 3600 - m * 60
c += s
if c >= 60:
    b += c // 60
    c %= 60
b += m
if b >= 60:
    a += b // 60
    b %= 60
a += h
if a >= 24:
    a %= 24
print(a, b, c)
