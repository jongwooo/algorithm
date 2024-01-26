import sys
from collections import deque


def input():
    return sys.stdin.readline().rstrip()


n = int(input())
balloons = deque(enumerate(map(int, input().split()), start=1))
exploded = []
while balloons:
    i, paper = balloons.popleft()
    exploded.append(i)
    balloons.rotate(-paper + 1 if paper > 0 else -paper)
print(*exploded)
