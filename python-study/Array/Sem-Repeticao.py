lista_de_unicos = []
contin = 'S'
while contin in 'Ss':
    num = int(input('Digite um número:'))
    if num not in lista_de_unicos:
        lista_de_unicos.append(num)
    contin = input('Continuar?[S/N]').upper()
    while contin not in 'SN':
        contin = input('Continuar?[S/N]').upper()
lista_de_unicos.sort()
print(f'A lista é: ', lista_de_unicos)
