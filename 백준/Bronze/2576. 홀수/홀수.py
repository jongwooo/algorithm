import sys

odd = []
for _ in range(7):
    n = int(sys.stdin.readline())
    if n % 2 == 1:
        odd.append(n)
if odd:
    print(sum(odd))
    print(min(odd))
else:
    print(-1)
