time = []
jog = {}
while True:
    jog.clear()
    jog = {'nome': input('Nome do Jogador: '), 'gols': [], 'total': 0, 'njogos': int(input('Número de Jogos:'))}
    for j in range(jog["njogos"]):
        jog['gols'].append(int(input(f'Quantos gols no {j + 1}° jogo: ')))
    for g in jog['gols']:
        jog['total'] += g
    time.append(jog.copy())
    cont = input('Continuar?[S/N]').upper()
    while cont not in 'SN':
        print('Somente valores S ou N')
        cont = input('Continuar?[S/N]').upper()
    if cont in 'N':
        break
print('-='*30)
print('Resultado:')
print(f'{"N°":>3}', end=' ')
for i in jog.keys():
    print(f'{i:<15}',end='')
print()
for k, v in enumerate(time):
    print(f'{1 + k:^4}', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='*30)
detalhe=int(input('Detalhe de Jogador(0>cancela): '))
while detalhe != 0:
    print('-=' * 20)
    print(f'O jogador {time[detalhe-1]["nome"]} jogou {time[detalhe-1]["njogos"]} partidas :')
    for j, g in enumerate(time[detalhe-1]['gols']):
        print(f' => Na {j + 1}° partida fez {g} gols.')
    print(f' Foi um total de {time[detalhe-1]["total"]} gols!')
    print()
    detalhe=int(input('Detalhe de Jogador(0>cancela): '))
print('<<<<FIM>>>>')
