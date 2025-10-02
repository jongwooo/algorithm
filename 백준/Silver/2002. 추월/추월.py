import sys

n = int(sys.stdin.readline())
in_order = dict()
out = []
for i in range(1, n + 1):
    car = sys.stdin.readline().rstrip()
    in_order[car] = i
for _ in range(n):
    car = sys.stdin.readline().rstrip()
    out.append(in_order[car])
pass_cnt = 0
for i in range(n):
    for j in range(i + 1, n):
        if out[i] > out[j]:
            pass_cnt += 1
            break
print(pass_cnt)
