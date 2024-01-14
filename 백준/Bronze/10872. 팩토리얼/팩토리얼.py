def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num - 1)


n = int(input())
print(factorial(n))
