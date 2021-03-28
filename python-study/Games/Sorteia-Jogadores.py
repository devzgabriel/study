import random
from time import sleep
from operator import itemgetter

jogadores = {'jog1': random.randint(1, 6), 'jog2': random.randint(1, 6), 'jog3': random.randint(1, 6),
             'jog4': random.randint(1, 6)}
for k, v in jogadores.items():
    print(f'`{k} tirou {v} no dado')
    sleep(1)
print('+=' * 20)
rank = []
#itemgeter(1) => pega o valor
rank = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(rank):
    print(f'{i + 1}° lugar: {v[0]} com {v[1]} pontos.')
    sleep(1)
print('+=' * 20)
