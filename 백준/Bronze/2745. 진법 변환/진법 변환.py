number = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
n, b = input().split()
ans = 0
for i, num in enumerate(n[::-1]):
    ans += int(b) ** i * number.index(num)
print(ans)
