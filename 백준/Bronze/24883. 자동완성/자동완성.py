import sys

alphabet = sys.stdin.readline().rstrip()
print('Naver D2' if alphabet == 'n' or alphabet == 'N' else 'Naver Whale')
