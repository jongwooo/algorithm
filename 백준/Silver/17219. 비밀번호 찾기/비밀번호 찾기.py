n, m = map(int, input().split())
auth = {}
for _ in range(n):
    site, password = input().split()
    auth[site] = password
for _ in range(m):
    site = input()
    print(auth[site])
