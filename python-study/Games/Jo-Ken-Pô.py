# ------------------------------------------------- Jo-ken-pô
from random import choice

jogadas = ['pedra', 'papel', 'tesoura']
jogador = int(input('Jokenpô \n 1-Pedra \n 2-Papel \n 3-Tesoura'))
if jogador == 1:
    if choice(jogadas) == [0]:
        print('Empate')
    elif choice(jogadas) == [1]:
        print('Você perdeu')
    else:
        print('Você venceu')
elif jogador == 2:
    if choice(jogadas) == [0]:
        print('Você venceu')
    elif choice(jogadas) == [1]:
        print('Empate')
    else:
        print('Você perdeu')
elif jogador == 3:
    if choice(jogadas) == [0]:
        print('Você perdeu')
    elif choice(jogadas) == [1]:
        print('Você venceu')
    else:
        print('Empate')
