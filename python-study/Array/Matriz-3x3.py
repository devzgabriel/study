matriz = [[[], [], []],
          [[], [], []],
          [[], [], []]]
maior_n = soma_pares = 0

print('Digite os valores para a Matriz 3x3:')
for lin in range(3):
    for col in range(3):
        matriz[lin][col] = float(input(f'Valor para: {lin + 1}x{col + 1} '))
for lin in range(3):
    for col in range(3):
        print(f'[{matriz[lin][col]:^5}]', end='')
    print()
for lin in range(3):
    for col in range(3):
        if matriz[lin][col] % 2 == 0:
            soma_pares += matriz[lin][col]
        if matriz[lin][col] > maior_n:
            maior_n = matriz[lin][col]
print(f'A soma dos pares é {soma_pares}, o maior número é {maior_n}')
