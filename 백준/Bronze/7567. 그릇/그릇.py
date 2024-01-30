import sys


dishes = sys.stdin.readline().rstrip()
height = 0
temp = ''
for dish in dishes:
    if temp != dish:
        temp = dish
        height += 10
    else:
        height += 5
print(height)
