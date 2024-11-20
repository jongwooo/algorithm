import sys

t = int(sys.stdin.readline())

for _ in range(t) :
  x = sys.stdin.readline().rstrip()
  data = []
  result = 0
  for i in range(len(x)) :
    if int(x[i]) not in data :
      result += 1
      data.append(int(x[i]))
  print(result)