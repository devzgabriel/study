def ficha(nome='null', gols=0):
    if nome not in 'null':
        print(f'O jogador {nome} fez {gols} gol(s).')
    else:
        print('O jogador não foi cadastrado')


jog = input('Nome do jogador: ')
if jog in '':
    ficha(gols=0)
else:
    gol = int(input('Gols do Jogador: '))
    
ficha(jog, gol)
