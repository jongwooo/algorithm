import sys

n = int(sys.stdin.readline())
result = ''
if n == 0:
    result += '0'
else:
    while n != 0:
        if n % -2 == 0:
            result += '0'
            n //= -2
        else:
            result += '1'
            n = (n - 1) // -2
print(result[::-1])
