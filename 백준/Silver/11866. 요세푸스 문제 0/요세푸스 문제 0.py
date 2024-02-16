import sys
from collections import deque

n, k = map(int, sys.stdin.readline().split())
queue = deque([i for i in range(1, n + 1)])
result = []
while queue:
    for _ in range(k - 1):
        queue.append(queue.popleft())
    result.append(str(queue.popleft()))
print(f'<{", ".join(result)}>')
