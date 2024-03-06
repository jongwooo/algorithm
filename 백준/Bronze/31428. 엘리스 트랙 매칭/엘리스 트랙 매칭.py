import sys

n = int(sys.stdin.readline())
friends = sys.stdin.readline().rstrip().split()
hello_bit = sys.stdin.readline().rstrip()
print(friends.count(hello_bit))
