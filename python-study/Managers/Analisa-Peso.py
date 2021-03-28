tab_pesos = list()
pessoa = list()
men_peso = mai_peso = 0
p_leve = 'NULL'
p_pesada = 'NULL'
cont = 'S'
while cont in 'S':
    pessoa.append(str(input('Nome:')))
    pessoa.append(int(input('Peso:')))
    tab_pesos.append(pessoa[:])
    men_peso = pessoa[1]
    mai_peso = pessoa[1]
    pessoa.clear()
    cont = input('Continuar?[S/N]').upper()
    while cont not in 'SN':
        cont = input('Continuar?[S/N]').upper()
for c in range(0, len(tab_pesos)):
    if tab_pesos[c][1] > mai_peso:
        mai_peso = tab_pesos[c][1]
        p_pesada = tab_pesos[c][0]
    if tab_pesos[c][1] < men_peso:
        men_peso = tab_pesos[c][1]
        p_leve = tab_pesos[c][0]
print(
    f'''Foram cadastradas {len(tab_pesos)} pessoas.
A mais leve  tem {men_peso}Kg. Nome(s): ''', end='')
for p in tab_pesos:
    if p[1] == mai_peso:
        print(p[0], end='   ')
print()
print(f'A mais pesada tem {mai_peso}Kg. Nome(s): ', end='')
for p in tab_pesos:
    if p[1] == men_peso:
        print(p[0], end='   ')
