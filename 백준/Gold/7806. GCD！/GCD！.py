import sys

while True:
    try:
        n, k = map(int, sys.stdin.readline().split())
        result = 1
        if n == 0:
            n = 1
        for i in range(2, int(k ** 0.5) + 1):
            pk, pn = 0, 0
            while k % i == 0:
                k //= i
                pk += 1
            if pk > 0:
                j = i
                while j <= n:
                    pn += n // j
                    j *= i
            result *= i ** min(pk, pn)
            if k < i:
                break
        if 1 < k < n:
            result *= k
        print(result)
    except:
        break
