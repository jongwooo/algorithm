import sys

science = sorted([int(sys.stdin.readline()) for _ in range(4)], reverse=True)
social_study = sorted([int(sys.stdin.readline()) for _ in range(2)], reverse=True)
print(sum(science[:3]) + social_study[0])
