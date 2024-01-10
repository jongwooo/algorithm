mul = 1
for _ in range(3):
    mul *= int(input())
mul_str = str(mul)
for i in range(10):
    print(mul_str.count(str(i)))
