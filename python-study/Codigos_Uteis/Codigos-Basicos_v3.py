# ------------------------------------------------- Jogo do acerto
import random

a = int(random.randrange(0, 5))
i = int(input('Digite um número entre 1 e 5: '))
if a == i:
    print('\032[32mVoce acertou!\033[m')
else:
    print('\033[31mVoce errou!\033[m')

# ------------------------------------------------- Velocimetro Multa
v = float(input('Qual a velocidade do carro? '))
if v > 80.0:
    print('A multa vai custar 7 reais a cada km acima do limite,total de {} reais'.format((v - 80) * 7))

# ------------------------------------------------- Par ou Impar
n = int(input('Digite um número: '))
resultado = n % 2
if resultado == 1:
    print('esse número é impar')
else:
    print('esse número é par')

# ------------------------------------------------- Preço da passagem
valor = float(input('Qual a distancia da viagem? '))
if valor <= 200:
    print('o valor da passagem é:{:.2f} reais'.format(valor * 0.5))
else:
    print('O valor da passagem é {:.2f} reais'.format(valor * 0.45))

# ------------------------------------------------- Ano Bisexto
ano = float(input('Qual o ano? '))
if ano % 4 == 0:
    print('esse ano é bisexto')
else:
    print('esse ano nao é bisexto')

# ------------------------------------------------- Aumento de salário
salario = float(input('Qual o salário? '))
if salario > 1250:
    print('novo salário é {:.2f} '.format((salario * 10 / 100) + salario))
else:
    print('novo salario é {:.2f} '.format((salario * 15 / 100) + salario))

# ------------------------------------------------- Analise numero na lista

numeros = (int(input('Um número:')),
           int(input('Outro número:')),
           int(input('Outro número:')),
           int(input('Outro número:')))
print(f'O numero 9 aparece {numeros.count(9)} vezes')
if 3 in numeros:
    print(f'O numero 3 aparece na posiçao: {numeros.index(3)+1}°')
else:
    print('O número 3 não foi digitado')
print('Os pares são:', end=' ')
for n in numeros:
    if n % 2 == 0:
        print(n, end='  ')

# ------------------------------------------------- Analise Voto

from datetime import datetime


# exercicio 101
def voto(i):
    if i < 16:
        return f'Voto Negado com {i} anos'
    elif (i < 18) or (i >= 60):
        return f'Voto Opicional com {i} anos'
    else:
        return f'Voto Obrigatório com {i} anos'


idade = datetime.now - (int(input('Nascimento: ')))
print(voto(idade))

# ------------------------------------------------- Teste de numero
def leiaint(txt):
    while True:
        valor = input(txt)
        if valor.isnumeric():
            return valor
        else:
            print(f'\033[0;31mNão é um número válido!\033[m')


n = leiaint('Digite um numero: ')
print(f'Você digitou o número inteiro {n}')

