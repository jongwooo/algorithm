import sys

input = sys.stdin.readline

n = int(input())
counting = [0] * 10001
for _ in range(n):
    counting[int(input())] += 1
for i in range(len(counting)):
    if counting[i] != 0:
        for _ in range(counting[i]):
            print(i)
            counting[i] -= 1
