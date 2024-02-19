import sys

while True:
    try:
        n = int(sys.stdin.readline())
    except:
        break
    multiple = 1
    digit = 1
    while True:
        if multiple % n == 0:
            print(digit)
            break
        multiple = multiple * 10 + 1
        digit += 1
