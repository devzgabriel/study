
# ------------------------------------------------- Tabuada
tab = int(input('Qual o nmero da tabuada? '))
for n in range(1, 11):
    print('{} x {}= '.format(n, tab), n * tab)

# ------------------------------------------------- Soma 6 pares
pares = []
print('Digite 6 Números')
for n in range(0, 6):
    num_de_entrada = int(input())
    if num_de_entrada % 2 == 0:
        pares.append(num_de_entrada)
print('A soma é: ', sum(pares))
# ------------------------------------------------- 10 termos da Sequencia PG
prim = int(input('Primeiro termo: '))
seq = int(input('Sequencia PG: '))
for sequen in range(prim, 11 * seq, seq):
    print(sequen)

# -------------------------------------------------
def leiaint(txt):
    while True:
        valor = input(txt).strip()
        if valor.isnumeric():
            return valor
        else:
            print(f'\033[0;31mNão é um número válido!\033[m')


def leiafloat(txt):
    while True:
        i = input(txt).strip()
        try:
            float(i)
            return i
        except:
            print(f'\033[0;33mDigite um numero Real válido!!\033[m')

# ------------------------------------------------- Mostra Fun.Trigonomérticas

import math

angulo = float(input('Digite um ãlgulo: '))
arad = math.radians(angulo)
print('O seno de {} é {:.2f}'.format(angulo, math.sin(arad)))
print('O cosseno de {} é {:.2f}'.format(angulo, math.cos(arad)))
print('A tangente de {} é {:.2f}'.format(angulo, math.tan(arad)))

# ------------------------------------------------- Descobre Hipotenusa
c1 = int(input('Qual o cateto 1?'))
c2 = int(input('Qual o cateto 2?'))
hip = (c1 ** 2 + c2 ** 2) ** (1 / 2)
print(hip)

