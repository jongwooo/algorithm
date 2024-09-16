import sys


def dfs(idx, value):
    global result
    if n == idx:
        result = max(result, int(value))
        return
    if idx + 4 <= n:
        dfs(idx + 4, str(eval(''.join([value, expression[idx]] + [str(eval(''.join(expression[idx + 1:idx + 4])))]))))
    if idx + 2 <= n:
        dfs(idx + 2, str(eval(''.join([value] + expression[idx:idx + 2]))))


n = int(sys.stdin.readline())
expression = list(sys.stdin.readline().rstrip())
result = -float(1e9)
dfs(1, expression[0])
print(result)
