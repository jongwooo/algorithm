import sys
import math


def area(x1, y1, r1, x2, y2, r2):
    d = math.sqrt(pow(x2 - x1, 2) + pow(y2 - y1, 2))
    rr1 = r1 ** 2
    rr2 = r2 ** 2
    if d > r2 + r1:
        return 0
    if d <= abs(r1 - r2) and r1 < r2:
        return math.pi * rr1
    if d <= abs(r1 - r2) and r1 >= r2:
        return math.pi * rr2
    phi = (math.acos((rr1 + (d * d) - rr2) / (2 * r1 * d))) * 2
    theta = (math.acos((rr2 + (d * d) - rr1) / (2 * r2 * d))) * 2
    area1 = 0.5 * rr2 * (theta - math.sin(theta))
    area2 = 0.5 * rr1 * (phi - math.sin(phi))
    return area1 + area2


x1, y1, r1, x2, y2, r2 = map(float, sys.stdin.readline().split())
result = float(round(1_000 * area(x1, y1, r1, x2, y2, r2)) / 1_000)
print('%.3f' % result)
