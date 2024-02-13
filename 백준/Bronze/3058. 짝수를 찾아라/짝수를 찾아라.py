import sys

t = int(sys.stdin.readline())
for _ in range(t):
    nums = sorted(list(map(int, sys.stdin.readline().split())))
    even = []
    for n in nums:
        if n % 2 == 0:
            even.append(n)
    print(sum(even), even[0])
