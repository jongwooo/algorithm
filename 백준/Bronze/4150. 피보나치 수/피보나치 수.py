import sys

n = int(sys.stdin.readline())
f = [0, 1, 1]
for i in range(3, n + 1):
    num = f[i - 1] + f[i - 2]
    f.append(num)
print(f[n])
