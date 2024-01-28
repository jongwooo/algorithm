import sys

total = 0
tree_dict = dict()
for line in sys.stdin:
    if line == '\n':
        break
    tree = line.rstrip()
    total += 1
    if tree not in tree_dict:
        tree_dict[tree] = 1
    else:
        tree_dict[tree] += 1
sorted_tree_dict = sorted(tree_dict.items(), key=lambda x: x[0])
for tree, cnt in sorted_tree_dict:
    per = round(cnt / total * 100, 4)
    print(tree, '%.4f' % per)
