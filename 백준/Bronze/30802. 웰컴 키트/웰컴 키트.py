import sys

n = int(sys.stdin.readline())
sizes = list(map(int, sys.stdin.readline().split()))
t, p = map(int, sys.stdin.readline().split())
t_bundle = 0
for size in sizes:
    if size == 0:
        continue
    elif size <= t:
        t_bundle += 1
    elif size % t == 0:
        t_bundle += size // t
    else:
        t_bundle += size // t + 1
p_bundle = n // p
pen = n % p
print(t_bundle)
print(f'{p_bundle} {pen}')
