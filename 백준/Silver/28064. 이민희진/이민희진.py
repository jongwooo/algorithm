import sys

n = int(sys.stdin.readline())
name = [sys.stdin.readline().rstrip() for _ in range(n)]
cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        name1, name2 = name[i], name[j]
        for k in range(1, min(len(name1), len(name2)) + 1):
            if name1[len(name1) - k:] == name2[:k] or name2[len(name2) - k:] == name1[:k]:
                cnt += 1
                break
print(cnt)
