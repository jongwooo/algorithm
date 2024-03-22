import sys

a, b, c, d = map(int, sys.stdin.readline().split())
delivery = list(map(int, sys.stdin.readline().split()))
for i in delivery:
    dog = 0
    if 0 < i % (a + b) <= a:
        dog += 1
    if 0 < i % (c + d) <= c:
        dog += 1
    print(dog)
