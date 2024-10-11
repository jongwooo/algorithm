import sys

grades = (0, 4, 11, 23, 40, 60, 77, 89, 96, 100)
N, K = map(int, input().split())
G = list(map(int, input().split()))
for g in G:
    for i in range(1, len(grades)):
        if g * 100 // N <= grades[i]:
            print(i, end=' ')
            break
