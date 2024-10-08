import sys

clubs = {
    'M': 'MatKor',
    'W': 'WiCys',
    'C': 'CyKor',
    'A': 'AlKor',
    '$': '$clear'
}
print(clubs[sys.stdin.readline().rstrip()])
