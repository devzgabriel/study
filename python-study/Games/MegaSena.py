import random
from time import sleep

qtd_jogos = int(input('Quantos Jogos Gerar?'))
cont_jogos = num_jogo = 0
jogo = []
while cont_jogos < qtd_jogos:
    if len(jogo) < 6:
        num_jogo = random.randint(1, 60)
        if num_jogo not in jogo:
            jogo.append(num_jogo)
    else:
        cont_jogos += 1
        print(f'Jogo {cont_jogos} >>> {jogo}')
        jogo.clear()
        sleep(1)
