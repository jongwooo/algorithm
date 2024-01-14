length = int(input())
string = input()
alphabets = ' abcdefghijklmnopqrstuvwxyz'
hash_num = 0
for i in range(length):
    hash_num += alphabets.index(string[i]) * 31 ** i
print(hash_num % 1234567891)
