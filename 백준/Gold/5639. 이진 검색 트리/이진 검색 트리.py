import sys

sys.setrecursionlimit(10 ** 9)


def traversal(arr):
    if not arr:
        return
    mid = arr[0]
    left, right = [], []
    for i in range(1, len(arr)):
        if arr[i] > mid:
            left = arr[1:i]
            right = arr[i:]
            break
    if not left and not right:
        left = arr[1:]
    traversal(left)
    traversal(right)
    print(mid)


preorder = []
while True:
    try:
        preorder.append(int(sys.stdin.readline()))
    except:
        break
traversal(preorder)
