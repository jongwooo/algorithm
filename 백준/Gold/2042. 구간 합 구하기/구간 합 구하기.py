import sys


def init(start, end, index):
    if start == end:
        segment_tree[index] = nums[start - 1]
        return segment_tree[index]
    mid = (start + end) // 2
    segment_tree[index] = init(start, mid, 2 * index) + init(mid + 1, end, 2 * index + 1)
    return segment_tree[index]


def find(start, end, index, left, right):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return segment_tree[index]
    mid = (start + end) // 2
    return find(start, mid, 2 * index, left, right) + find(mid + 1, end, 2 * index + 1, left, right)


def update(start, end, index, update_index, data):
    if start > update_index or end < update_index:
        return
    segment_tree[index] += data
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, 2 * index, update_index, data)
    update(mid + 1, end, 2 * index + 1, update_index, data)


n, m, k = map(int, sys.stdin.readline().split())
nums = [int(sys.stdin.readline()) for _ in range(n)]
segment_tree = [0] * (n * 4)
init(1, n, 1)
for _ in range(m + k):
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 1:
        num = c - nums[b - 1]
        nums[b - 1] = c
        update(1, n, 1, b, num)
    if a == 2:
        print(find(1, n, 1, b, c))
