# ------------------------------------------------- Par ou Impar
import random

print('-' * 20)
print('Jogo:Par ou Impar')
print('-' * 20)
sequencia = 0
while True:
    p_i = input('Par ou Impar[P/I]: ')
    num = int(input('Qual o número: '))
    num_pc = random.randrange(1, 10)
    print(f'Minha escolha foi {num_pc}')
    if (num + num_pc) % 2 == 0 and p_i in 'Pp':
        sequencia += 1
        print('Voce Venceu... Vamos jogar de novo')
    elif (num + num_pc) % 2 == 1 and p_i in 'Ii':
        sequencia += 1
        print('Voce Venceu... Vamos jogar de novo')
    else:
        break
print(f'Voce perdeu após ganhar {sequencia} vezes')