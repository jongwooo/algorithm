import sys

n, q = map(int, sys.stdin.readline().split())
value = n
arr = [1] * n
for _ in range(q):
    q, *a = map(int, sys.stdin.readline().split())
    match q:
        case 1:
            index = a[0] - 1
            value -= arr[index]
            arr[index] = min(0, arr[index])
        case 2:
            index = a[0] - 1
            value += 1 - arr[index]
            arr[index] = max(1, arr[index])
        case 3:
            print(value)
