import sys

while True:
    try:
        n, k = map(int, sys.stdin.readline().split())
        chicken = n
        while True:
            if n // k == 0:
                break
            chicken += n // k
            n = (n // k) + n % k
        print(chicken)
    except:
        break
