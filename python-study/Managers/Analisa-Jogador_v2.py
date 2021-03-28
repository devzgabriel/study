jog = {'nome': input('Nome do Jogador: '), 'gols': [], 'total': 0}
njogos = int(input('Número de Jogos:'))
for j in range(njogos):
    jog['gols'].append(int(input(f'Quantos gols no {j + 1}° jogo: ')))
for g in jog['gols']:
    jog['total'] += g
print('-=' * 20)
print(jog)
print('-=' * 20)
for k, v in jog.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 20)
print(f'O jogador {jog["nome"]} jogou {njogos} partidas :')
for j, g in enumerate(jog['gols']):
    print(f' => Na {j + 1}° partida fez {g} gols.')
print(f' Foi um total de {jog["total"]} gols!')
