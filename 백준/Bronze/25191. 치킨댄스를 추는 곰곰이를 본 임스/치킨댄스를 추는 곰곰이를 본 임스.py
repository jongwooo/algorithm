import sys

chicken = int(sys.stdin.readline())
coke, beer = map(int, sys.stdin.readline().split())
eat = coke // 2 + beer
print(eat if chicken >= eat else chicken)
