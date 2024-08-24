import sys


def init(start, end, index):
    if start == end:
        segment_tree[index] = 0
        return
    mid = (start + end) // 2
    init(start, mid, 2 * index)
    init(mid + 1, end, 2 * index + 1)
    segment_tree[index] = segment_tree[2 * index] + segment_tree[2 * index + 1]


def query(start, end, index, left, right):
    if start > right or end < left:
        return 0
    if start >= left and end <= right:
        return segment_tree[index]
    mid = (start + end) // 2
    return query(start, mid, 2 * index, left, right) + query(mid + 1, end, 2 * index + 1, left, right)


def update(start, end, index, update_index, data):
    if start > update_index or end < update_index:
        return
    if start == end:
        segment_tree[index] = data
        return
    mid = (start + end) // 2
    update(start, mid, 2 * index, update_index, data)
    update(mid + 1, end, 2 * index + 1, update_index, data)
    segment_tree[index] = segment_tree[2 * index] + segment_tree[2 * index + 1]


n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
segment_tree = [0] * (n * 4)
init(1, n, 1)
total = 0
arr = sorted([(a[i], i + 1) for i in range(n)])
for i in range(n):
    _, idx = arr[i]
    total += query(1, n, 1, idx + 1, n)
    update(1, n, 1, idx, 1)
print(total)
