class Node:
    data = 0
    parent = 0
    left_child = 0
    right_child = 0

    def __init__(self, data):
        self.data = data


def traversal(node):
    global size
    size += 1
    if node.left_child != 0:
        traversal(nodes[node.left_child])
    if node.right_child != 0:
        traversal(nodes[node.right_child])


T = int(input())
for test_case in range(1, T + 1):
    V, E, v1, v2 = map(int, input().split())
    nodes = [Node(i) for i in range(V + 1)]
    links = list(map(int, input().split()))
    for i in range(E):
        p = links[2 * i]
        c = links[2 * i + 1]
        if nodes[p].left_child == 0:
            nodes[p].left_child = c
        else:
            nodes[p].right_child = c
        nodes[c].parent = p
    v1_node = nodes[v1]
    v2_node = nodes[v2]
    visited = [0] * (V + 1)
    common_parent = nodes[1]
    while v1_node.data != 1:
        visited[v1_node.data] = 1
        v1_node = nodes[v1_node.parent]
    while v2_node.data != 1:
        if visited[v2_node.data]:
            common_parent = v2_node
            break
        visited[v2_node.data] = 1
        v2_node = nodes[v2_node.parent]
    size = 0
    traversal(common_parent)
    print(f'#{test_case} {common_parent.data} {size}')
