from random import choice   # serve para escolher
from random import shuffle  # serve para embaralhar
qtd_opc = int(input('Quantas opções: '))
lista_opc = list()
for o in range(qtd_opc):
    lista_opc.append(input(f'Qual o {o+1}° item da lista:'))

print('O item sorteado foi:{}'.format(choice(lista_opc)))
shuffle(lista_opc)
print('A ordem sorteada foi:', lista_opc)
