lista_pessoas = []
pessoa = {}
media = 0
mulheres=[]
maior_idade=[]
while True:
    pessoa.clear()
    pessoa['Nome'] = input('Nome: ')
    pessoa['Idade'] = float(input('Idade: '))
    pessoa['Gênero'] = input('Gênero[M/F]: ').upper()[0]
    while pessoa["Gênero"] not in 'MF':
        print('Preencha somente com M ou F!')
        pessoa['Gênero'] = input('Gênero[M/F]: ').upper()[0]
    lista_pessoas.append(pessoa.copy())
    continuar = input('Continuar[S/N]: ').upper()[0]
    while continuar not in 'SN':
        print('Preencha somente com S ou N!')
        continuar = input('Continuar[S/N]: ').upper()[0]
    if continuar in 'N':
        break
print('-=' * 20)
print(lista_pessoas)
print(f'{len(lista_pessoas)} pessoas foram cadastradas.')
for p, i in enumerate(lista_pessoas):
    media += lista_pessoas[p]['Idade']
    if lista_pessoas[p]['Gênero'] in 'F':
        mulheres.append(lista_pessoas[p]['Nome'])
media = media / len(lista_pessoas)
for p, i in enumerate(lista_pessoas):
    if lista_pessoas[p]['Idade'] > media:
        maior_idade.append(lista_pessoas[p]['Nome'])
print(f'A média das idades é {media:.2f}')
print(f'As mulheres cadastradas são: {mulheres[:]}.')
print(f'As pessoas com idade acima da média são: {maior_idade}')
