
grenal = []
inter, gremio = map(int, input().split())
golint = inter
golgrem = gremio
vitinter = 0
vitgrem = 0
empate = 0
jogo = [inter, gremio]
grenal.append(jogo)
cont = int(input('Novo grenal (1-sim 2-nao)'))
if inter > gremio:
    vitinter += 1
elif gremio > inter:
    vitgrem += 1
elif gremio == inter:
    empate += 1
while cont == 1:
    inter, gremio = map(int, input().split())
    jogo = [inter, gremio]
    grenal.append(jogo)
    golint += inter
    golgrem += gremio
    if inter > gremio:
        vitinter += 1
    elif gremio > inter:
        vitgrem += 1
    cont = int(input('Novo grenal (1-sim 2-nao)'))
print('{} grenais'.format(len(grenal)))
print('Inter:{}'.format(vitinter))
print('Gremio:{}'.format(vitgrem))
print('Empates:{}'.format(empate))
if vitinter > vitgrem:
    print('Inter venceu mais')
elif vitgrem > vitinter:
    print('Gremio venceu mais')
elif vitgrem == vitinter:
    print('Nao houve vencedor')
