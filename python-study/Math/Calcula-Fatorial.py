def fatorial(num, show=False):
    fat = 1
    for f in range(num, 1, -1):
        fat *= f
        if show is True:
            print(f'{f} x ', end=' ')
    if show is True:
        print(f'= {fat}')
    else:
        print(f'O fatorial de {num} é {fat}')


n = int(input('N° para fatorial: '))
sow = bool(input('Mostrar calculo[True/False]: '))
fatorial(n, sow)
