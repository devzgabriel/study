lista = ('lapis', 1.50, 'borracha', 2.00,
         'caderno', 10.00, 'estojo', 7.00,
         'mochila', 80.00, 'canetas', 22.50, 'livros', 34.90)
for pos in range(len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<30}', end='R$')
    elif pos % 2 == 1:
        print(f'{lista[pos]:>.2f}')
