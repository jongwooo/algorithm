import sys


def print_ipv6(ipv6):
    groups = []
    for group in ipv6:
        groups.append('0' * (4 - len(group)) + group)
    print(':'.join(groups))


short_ipv6 = sys.stdin.readline().rstrip().split(':')
if len(short_ipv6) > 8:
    if short_ipv6[0] == '':
        short_ipv6 = short_ipv6[1:]
    elif short_ipv6[-1] == '':
        short_ipv6 = short_ipv6[:-1]
    print_ipv6(short_ipv6)
else:
    target = 0
    for i in range(len(short_ipv6)):
        if short_ipv6[i] == '':
            short_ipv6[i] = '0000'
            target = i
            continue
        if short_ipv6[i].isdigit() and int(short_ipv6[i]) == 0:
            short_ipv6[i] = '0000'
    for _ in range(8 - len(short_ipv6)):
        short_ipv6.insert(target, '0000')
    print_ipv6(short_ipv6)
