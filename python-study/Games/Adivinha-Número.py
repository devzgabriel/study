# ------------------------------------------------- Jogo do acerto
import random

dificult = int(input('Dificuldade   (Digite um Número) : '))
choice = int(random.randrange(0, dificult))
input_number = int(input('Digite um número entre 1 e 5: '))
errors = 0
if input_number != choice:
    while input_number != choice:
        errors += 1
        print('\033[31mVoce errou!Tente Novamente...\033[m')
        input_number = int(input('Digite um número entre 1 e 5: '))
else:
    print(f'\032[32mVoce acertou após errar {errors} vezes!\033[m')
