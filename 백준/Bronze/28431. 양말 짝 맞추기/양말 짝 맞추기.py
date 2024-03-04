import sys

socks = set()
for _ in range(5):
    sock = sys.stdin.readline().rstrip()
    if sock not in socks:
        socks.add(sock)
    else:
        socks.remove(sock)
print(list(socks)[0])
