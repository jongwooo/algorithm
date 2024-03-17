import sys

a = list(sys.stdin.readline())
b = list(sys.stdin.readline().split())
for i in range(len(a)):
    for j in range(len(b)):
        if a[i] == b[j]:
            a[i] = a[i].lower()
            continue
print(''.join(a))
