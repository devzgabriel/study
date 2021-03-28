somaidade = 0
velho = ''
idadevelho = 0
tmulher = 0
for p in range(1, 5):
    print('-----{} pessoa-----'.format(p))
    nome = str(input('Nome da pessoa: ')).strip()
    idade = int(input('Idade dessa pessoa: '))
    sexo = str(input('Qual o genero [M/F]')).strip()
    somaidade += idade
    if p == 1 and sexo in 'Mm':
        velho = nome
        idadevelho = idade
    if sexo in 'Mm' and idade > idadevelho:
        nome = velho
        idadevelho = idade
    if sexo in 'Ff' and idade < 20:
        tmulher += 1
print('Idade média:', somaidade / 4)
print('O homem mais velho é {} e tem {} anos.'.format(velho, idadevelho))
print('Há {} mulheres menores d 20 anos'.format(tmulher))
