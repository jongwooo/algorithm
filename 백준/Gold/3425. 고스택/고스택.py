import sys


def execute(commands, num):
    gostack = [num]
    for cmd in commands:
        if cmd[:3] == 'NUM':
            x = int(cmd[4:])
            gostack.append(x)
        elif not gostack:
            return 'ERROR'
        elif cmd == 'POP':
            gostack.pop()
        elif cmd == 'INV':
            gostack[-1] *= -1
        elif cmd == 'DUP':
            gostack.append(gostack[-1])
        elif len(gostack) == 1:
            return 'ERROR'
        elif cmd == 'SWP':
            gostack[-1], gostack[-2] = gostack[-2], gostack[-1]
        elif cmd == 'ADD':
            temp = gostack.pop() + gostack.pop()
            if abs(temp) > 10 ** 9:
                return 'ERROR'
            gostack.append(temp)
        elif cmd == 'SUB':
            temp = -gostack.pop() + gostack.pop()
            if abs(temp) > 10 ** 9:
                return 'ERROR'
            gostack.append(temp)
        elif cmd == 'MUL':
            temp = gostack.pop() * gostack.pop()
            if abs(temp) > 10 ** 9:
                return 'ERROR'
            gostack.append(temp)
        elif cmd == 'DIV':
            a, b = gostack.pop(), gostack.pop()
            if a == 0:
                return 'ERROR'
            temp = abs(b) // abs(a)
            if (a > 0 and b < 0) or (a < 0 and b > 0):
                temp = -temp
            if abs(temp) > 10 ** 9:
                return 'ERROR'
            gostack.append(temp)
        elif cmd == 'MOD':
            a, b = gostack.pop(), gostack.pop()
            if a == 0:
                return 'ERROR'
            temp = abs(b) % abs(a)
            if b < 0:
                temp = -temp
            if abs(temp) > 10 ** 9:
                return 'ERROR'
            gostack.append(temp)
        else:
            return 'ERROR'

    if len(gostack) != 1:
        return 'ERROR'
    return gostack[0]


while True:
    commands = []
    while True:
        cmd = sys.stdin.readline().strip()
        if cmd == 'QUIT':
            quit()
        if cmd == 'END':
            break
        commands.append(cmd)
    n = int(sys.stdin.readline())
    for _ in range(n):
        num = int(sys.stdin.readline())
        print(execute(commands, num))
    print()
    sys.stdin.readline()
