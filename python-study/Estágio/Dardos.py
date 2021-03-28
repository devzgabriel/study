import math

nomes=[]
pontuaçao=[]
n_players = int(input())
for n in range(n_players):
    player = input()
    nomes.append(player)
for rodada in range(n_players):
    ponto = input().split
    for p in ponto:
        if '*' in p:
            ponto[ponto.index(p)] = p[:p.index('*')] * p[p.index('*')+1:]
        elif 'x' in p:
            ponto[ponto.index(p)] = -20



