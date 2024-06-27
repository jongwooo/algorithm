import sys

n = sys.stdin.readline().rstrip()
check = list()
check.append(list(n[:len(n) // 2]))
check.append(list(n[len(n) // 2:]))
ch = list()
ch.append(list(map(int, check[0])))
ch.append(list(map(int, check[1])))
print('LUCKY' if sum(ch[0]) == sum(ch[1]) else 'READY')
