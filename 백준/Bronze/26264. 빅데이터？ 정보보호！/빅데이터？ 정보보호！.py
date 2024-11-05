import sys

n = int(sys.stdin.readline())
attention = sys.stdin.readline().rstrip()
big_data = attention.count('bigdata')
security = attention.count('security')
if big_data > security:
    print('bigdata?')
elif big_data < security:
    print('security!')
else:
    print('bigdata? security!')
