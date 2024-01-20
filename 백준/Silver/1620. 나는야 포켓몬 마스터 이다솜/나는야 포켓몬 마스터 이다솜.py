import sys

input = sys.stdin.readline

n, m = map(int, input().split())
by_id = {}
by_name = {}
for i in range(1, n + 1):
    pokemon = input().rstrip()
    by_id[i] = pokemon
    by_name[pokemon] = i
for _ in range(m):
    x = input().rstrip()
    if x.isdigit():
        print(by_id[int(x)])
    else:
        print(by_name[x])
