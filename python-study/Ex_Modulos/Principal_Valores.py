import moeda

valor = int(input('Digite um valor:'))
print(f'O valor aumentado em 15% é {moeda.dinheiro(str(moeda.aumentar(valor, 15)))}')
print(f'O valor reduzido em 15% é {moeda.dinheiro(str(moeda.reduzir(valor, 15)))}')
print(f'O dobro de {moeda.dinheiro(str(valor))} é {moeda.dinheiro(str(moeda.dobro(valor)))}')
print(f'A metade do {moeda.dinheiro(str(valor))} é {moeda.dinheiro(str(moeda.metade(valor)))}')
