import sys

t = int(sys.stdin.readline())
n = int(sys.stdin.readline())
candy = list(map(int, sys.stdin.readline().split()))
print(f'Padaeng_i {"Happy" if t <= sum(candy) else "Cry"}')
