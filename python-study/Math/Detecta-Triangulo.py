r1 = input('digite os 3 comrimentos de reta: ')
r2 = input()
r3 = input()
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Formam um triangulo')
else:
    print('Esses comprimentos de reta não formam um triangulo')
