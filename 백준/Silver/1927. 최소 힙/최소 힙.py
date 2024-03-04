import sys
import heapq

n = int(sys.stdin.readline())
queue = []
for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        print(0 if not queue else heapq.heappop(queue))
    else:
        heapq.heappush(queue, x)
