import sys
from collections import deque

N, L = map(int, sys.stdin.readline().split())
A = list(map(int, sys.stdin.readline().split()))
queue = deque([])
for i in range(N):
    if queue and queue[0][0] < i - L + 1:
        queue.popleft()
    while len(queue) >= 1 and A[i] < queue[-1][1]:
        queue.pop()
    queue.append((i, A[i]))
    print(queue[0][1], end=' ')
