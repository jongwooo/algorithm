import sys
import math

rh, rv, sh, sv = map(int, sys.stdin.readline().split())
n = int(sys.stdin.readline())
min_price = int(1e9)
for _ in range(n):
    rhi, rvi, shi, svi, pi = map(int, sys.stdin.readline().split())
    a = math.ceil(max(rh / rhi, sh / shi)) * math.ceil(max(rv / rvi, sv / svi))
    b = math.ceil(max(rh / rvi, sh / svi)) * math.ceil(max(rv / rhi, sv / shi))
    min_price = min(min_price, min(a, b) * pi)
print(min_price)
