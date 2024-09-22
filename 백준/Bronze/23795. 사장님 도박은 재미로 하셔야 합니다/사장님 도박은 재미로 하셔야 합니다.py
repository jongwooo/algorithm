import sys
money_sum = 0
while True:
    money = int(sys.stdin.readline())
    if money < 0:
        break
    money_sum += money
print(money_sum)
