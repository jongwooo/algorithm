import sys

n = int(sys.stdin.readline())
price = int(sys.stdin.readline())
sale = [0]
if n >= 5:
    sale.append(500)
if n >= 10:
    sale.append(price // 10)
if n >= 15:
    sale.append(2000)
if n >= 20:
    sale.append(price // 4)
result = price - max(sale)
if result < 0:
    result = 0
print(result)
