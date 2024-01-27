import sys
import heapq


def input():
    return sys.stdin.readline()


n = int(input())
heap = []
for _ in range(n):
    nums = list(map(int, input().split()))
    for num in nums:
        if len(heap) < n:
            heapq.heappush(heap, num)
        elif heap[0] < num:
            heapq.heappop(heap)
            heapq.heappush(heap, num)
print(heap[0])
