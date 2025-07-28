import sys

scenario_num = 1
while True:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    names = []
    for _ in range(n):
        name = sys.stdin.readline().rstrip()
        names.append(name)
    a = [0] * n
    b = [0] * n
    for _ in range(2 * n - 1):
        num, flag = sys.stdin.readline().rstrip().split()
        idx = int(num) - 1
        if flag == 'A':
            a[idx] = 1
        if flag == 'B':
            b[idx] = 1
    no_return_girl_name = ""
    for i in range(n):
        if not a[i] or not b[i]:
            no_return_girl_name = names[i]
            break
    print(scenario_num, no_return_girl_name)
    scenario_num += 1
