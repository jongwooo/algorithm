import sys

alphabet = ' ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
n = int(sys.stdin.readline())
cipher = list(map(int, sys.stdin.readline().split()))
cipher_dic = {}
for c in cipher:
    if alphabet[c] not in cipher_dic:
        cipher_dic[alphabet[c]] = 1
    else:
        cipher_dic[alphabet[c]] += 1
plain_text = sys.stdin.readline().rstrip()
wrong = False
for p in plain_text:
    if p in cipher_dic and cipher_dic[p] > 0:
        cipher_dic[p] -= 1
    else:
        wrong = True
        break
print('n' if wrong else 'y')
