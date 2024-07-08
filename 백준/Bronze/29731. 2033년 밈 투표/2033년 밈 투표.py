import sys

promises = {
    'Never gonna give you up',
    'Never gonna let you down',
    'Never gonna run around and desert you',
    'Never gonna make you cry',
    'Never gonna say goodbye',
    'Never gonna tell a lie and hurt you',
    'Never gonna stop'
}
n = int(sys.stdin.readline())
flag = True
for _ in range(n):
    s = sys.stdin.readline().rstrip()
    if s not in promises:
        flag = False
print('No' if flag else 'Yes')
