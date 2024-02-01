import sys

n = int(sys.stdin.readline())
person = []
for _ in range(n):
    name, d, m, y = sys.stdin.readline().split()
    person.append((name, int(d), int(m), int(y)))
person.sort(key=lambda x: (x[3], x[2], x[1]))
print(person[-1][0])
print(person[0][0])
