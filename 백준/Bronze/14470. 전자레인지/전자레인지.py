import sys

a = int(sys.stdin.readline())
b = int(sys.stdin.readline())
c = int(sys.stdin.readline())
d = int(sys.stdin.readline())
e = int(sys.stdin.readline())
if a < 0:
    time = -a * c + d + b * e
else:
    time = (b - a) * e
print(time)
