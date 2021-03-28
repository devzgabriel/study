# exercicio 97
def escreva(om):
    print('-' * len(om))
    print(om)
    print('-' * len(om))
escreva(str(input('Frase:')))


# exercicio 99
def maior(num):
    if len(num) == 0:
        print(f'     >>>  Não foram detectados valores')
        print()
    else:
        for n in num:
            print(n, end=' ')
        print(f' >>>  Foram detectados {len(num)} valores e o maior é {max(num)}')
        print()


maior([5, 4, 7, 3, 8])
maior([3, 6, 5, 9])
maior([])
maior([2])

# exercicio 100
from random import randint

def sorteio():
    sor = []
    for c in range(5):
        sor.append(randint(1, 10))
    return sor


def somapares():
    pares = []
    soma = 0
    srt = sorteio()
    for n in srt:
        if n % 2 == 0:
            pares.append(n)
            soma += n
    return srt, pares, soma


resultado = somapares()
print('-='*30)
print(f'Os valores sorteados são {resultado[0]}')
print(f'Seus pares são {resultado[1]} e a soma deles é {resultado[2]}')
print('-='*30)
