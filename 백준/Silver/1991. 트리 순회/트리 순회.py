import sys


def preorder(node):
    if node != '.':
        print(node, end='')
        preorder(tree[node][0])
        preorder(tree[node][1])


def inorder(node):
    if node != '.':
        inorder(tree[node][0])
        print(node, end='')
        inorder(tree[node][1])


def postorder(node):
    if node != '.':
        postorder(tree[node][0])
        postorder(tree[node][1])
        print(node, end='')


n = int(sys.stdin.readline().strip())
tree = {}
for n in range(n):
    parent, left, right = sys.stdin.readline().split()
    tree[parent] = [left, right]
preorder('A')
print()
inorder('A')
print()
postorder('A')
