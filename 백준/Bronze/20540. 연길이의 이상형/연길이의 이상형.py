import sys

mbti_dict = {
    'I': 'E',
    'E': 'I',
    'S': 'N',
    'N': 'S',
    'T': 'F',
    'F': 'T',
    'P': 'J',
    'J': 'P'
}

mbti = sys.stdin.readline().rstrip()
for i in mbti:
    print(mbti_dict[i], end='')
