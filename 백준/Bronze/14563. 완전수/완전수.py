import sys

t = int(sys.stdin.readline())
n = list(map(int, sys.stdin.readline().split()))
for num in n:
    num_sum = 0
    for i in range(1, num):
        if num % i == 0:
            num_sum += i
    if num_sum == num:
        print('Perfect')
    elif num_sum > num:
        print('Abundant')
    else:
        print('Deficient')
