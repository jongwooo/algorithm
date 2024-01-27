import heapq
import sys


def input():
    return sys.stdin.readline()


n = int(input())
heap = []
cnt = 0
for _ in range(n):
    x = int(input())
    if x == 0:
        print(0 if not heap else -heapq.heappop(heap))
    else:
        heapq.heappush(heap, -x)
