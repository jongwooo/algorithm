import sys


def ccw(x1, y1, x2, y2, x3, y3):
    return (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)


x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
x3, y3, x4, y4 = map(int, sys.stdin.readline().split())
ccw123 = ccw(x1, y1, x2, y2, x3, y3)
ccw124 = ccw(x1, y1, x2, y2, x4, y4)
ccw341 = ccw(x3, y3, x4, y4, x1, y1)
ccw342 = ccw(x3, y3, x4, y4, x2, y2)
print(1 if ccw123 * ccw124 < 0 and ccw341 * ccw342 < 0 else 0)
