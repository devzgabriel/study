from random import randint
from time import sleep
b2=randint(1,30)
def natal():
    print('\033[7m')
    for x in range(1,23):
        b1= randint(1,b2)
        if x == 1:
            d='$'
        elif b1%4==0:
            d='o'
        elif b1%3==0:
            d='i'
        else:
            d='*'
        print('{:^33}'.format(x*d))
    sleep(1)
while True:
    natal()

