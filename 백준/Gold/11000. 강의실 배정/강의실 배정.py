import heapq
import sys

input = sys.stdin.readline

n = int(input())
classes = []
for _ in range(n):
    s, t = map(int, input().split())
    classes.append((s, t))
classes.sort()
room = []
heapq.heappush(room, classes[0][1])
for i in range(1, n):
    if classes[i][0] < room[0]:
        heapq.heappush(room, classes[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, classes[i][1])
print(len(room))
