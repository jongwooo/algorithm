import sys

t = int(sys.stdin.readline())
for _ in range(t):
    n = sys.stdin.readline().strip()
    s = str(int(n) + int(n[::-1]))
    print("YES" if s == s[::-1] else "NO")
