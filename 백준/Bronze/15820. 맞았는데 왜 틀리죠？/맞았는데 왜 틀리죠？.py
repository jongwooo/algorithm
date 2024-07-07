import sys

s1, s2 = map(int, sys.stdin.readline().split())
accepted, sample_tc, sys_tc = True, True, True
for _ in range(s1):
    sample, ans = map(int, sys.stdin.readline().split())
    if sample != ans:
        accepted = False
        sample_tc = False
for _ in range(s2):
    tc, ans = map(int, sys.stdin.readline().split())
    if tc != ans:
        accepted = False
        sys_tc = False
if accepted:
    print('Accepted')
elif not sample_tc:
    print('Wrong Answer')
elif sample_tc and not sys_tc:
    print('Why Wrong!!!')
