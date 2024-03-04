import sys

n = int(sys.stdin.readline())
participants = set()
for _ in range(2* n - 1):
    runner = sys.stdin.readline().rstrip()
    if runner in participants:
        participants.remove(runner)
    else:
        participants.add(runner)
print(list(participants)[0])
