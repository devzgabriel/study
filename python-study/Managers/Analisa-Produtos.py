nome_barato = ''
maisbarato = caros = total = contador = 0
contin = '42'
while True:
    contador += 1
    nome_p = str(input('Qual o nome do produto:'))
    preco_p = float(input('Preco do prduto:'))
    total += preco_p
    if contador == 1 or preco_p < maisbarato:
        maisbarato = preco_p
        nome_barato = nome_p
    if preco_p < maisbarato:
        nome_barato = nome_p
    if preco_p > 1000:
        caros += 1
    while contin not in 'SsNn':
        contin = input('Continuar?[S/N]')
    if contin in 'Nn':
        break
    contin = '42'
print(f'Total:{total} \n{caros} produtos custaram mais de R$ 1000 Reais\nMais barato: {nome_barato} custou R${maisbarato}')
