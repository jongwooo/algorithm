import sys

n = int(sys.stdin.readline())
for x in range(1, n + 1) :
  data = sys.stdin.readline().rstrip()
  result = ''
  for i in range(len(data)) :
    value = ord(data[i]) + 1
    if value > 90 :
      value = 65
    result += chr(value)
  print(f'String #{x}')
  print(result)
  print()
