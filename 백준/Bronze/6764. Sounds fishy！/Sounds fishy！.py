import sys

depths = [int(sys.stdin.readline()) for _ in range(4)]
r = 0
for i in range(3):
    if depths[i + 1] > depths[i]:
        r += 1
    elif depths[i + 1] < depths[i]:
        r -= 1
if len(set(depths)) == 1:
    print('Fish At Constant Depth')
elif r == 3:
    print('Fish Rising')
elif r == -3:
    print('Fish Diving')
else:
    print('No Fish')
