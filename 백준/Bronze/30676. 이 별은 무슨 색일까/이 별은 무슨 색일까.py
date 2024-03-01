import sys

lambda_value = int(sys.stdin.readline())
if 620 <= lambda_value <= 780:
    print('Red')
elif 590 <= lambda_value < 620:
    print('Orange')
elif 570 <= lambda_value < 590:
    print('Yellow')
elif 495 <= lambda_value < 570:
    print('Green')
elif 450 <= lambda_value < 495:
    print('Blue')
elif 425 <= lambda_value < 450:
    print('Indigo')
elif 380 <= lambda_value < 425:
    print('Violet')
