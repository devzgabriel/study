ced = 100
totced, totmoe = 0, 0
din = round(float(input()), 2)
print('NOTAS:')
while True:
    if din >= ced:
        din -= ced
        totced += 1
    else:
        print("{} nota(s) de R$ {:.2f}".format(totced, ced))
        totced = 0
        if ced == 100:
            ced = 50
        elif ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 5
        elif ced == 5:
            ced = 2
        else:
            ced = 1
            break
print('MOEDAS:')
while True:
    if din >= ced:
        din -= ced
        totced += 1
    else:
        print("{} moeda(s) de R$ {:.2f}".format(totced, ced))
        totced = 0
        if ced == 1:
            ced = 0.50
        elif ced == 0.50:
            ced = 0.25
        elif ced == 0.25:
            ced = 0.10
        elif ced == 0.10:
            ced = 0.05
        elif ced == 0.05:
            ced = 0.01
        else:
            break
