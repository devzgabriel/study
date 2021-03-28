# ------------------------------------------------- Emprestimo Casa
house = float(input('Qual o valor da casa?'))
salario = float(input('salário: '))
prazo = float(input('prazo em anos: '))
if house / (prazo * 24) > (3 / 10) * salario:
    print('Emréstimo não liberado')
else:
    print('Empréstimo liberado')

# ------------------------------------------------- Fogos reveillon
from time import sleep

for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('Boooom')

# ------------------------------------------------- Mostra pares
for par in range(2, 51, 2):
    print(par, end=',')

# ------------------------------------------------- Soma Impares
soma = 0
for imp in range(1, 501, 2):
    if imp % 3 == 0:
        soma = soma + imp
print('\n Soma:', soma)

# ------------------------------------------------- Soma 6 pares
pares = []
print('Digite 6 Números')
for n in range(0, 6):
    num_de_entrada = int(input())
    if num_de_entrada % 2 == 0:
        pares.append(num_de_entrada)
print('A soma é: ', sum(pares))
