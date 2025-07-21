import sys

n, k = sys.stdin.readline().split()
n = int(n)
peoples = set()
for _ in range(n):
    name = sys.stdin.readline().rstrip()
    peoples.add(name)
peoples_cnt = len(peoples)
if k == 'Y':
    print(peoples_cnt)
elif k == 'F':
    print(peoples_cnt // 2)
else:
    print(peoples_cnt // 3)
