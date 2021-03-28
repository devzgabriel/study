lista_entrada = []
pares = []
impares = []
contin = 'S'
while contin in 'Ss':
    num = int(input('Digite um número:'))
    if num not in lista_entrada:
        lista_entrada.append(num)
    contin = input('Continuar?[S/N]').upper()
    while contin not in 'SN':
        contin = input('Continuar?[S/N]').upper()
print(f'A lista é: ', lista_entrada)
for c in lista_entrada:
    if c % 2 == 0:
        pares.append(c)
    else:
        impares.append(c)
print(f'A lista par é: ', pares)
print(f'A lista impar é: ', impares)
