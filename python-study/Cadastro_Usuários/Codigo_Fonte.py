from Cadastro_Usuários import def_menu
from time import sleep

while True:
    opcao = def_menu.menu(['Ver Lista', 'Cadastrar pessoas', 'Sair do sistema'])
    if opcao == 1:
        def_menu.verlista('pessoas.txt')
        sleep(3)
    elif opcao == 2:
        nome = input('Nome: ').strip()
        while True:
            idade = input('Idade: ').strip()
            if not idade.isnumeric():
                print(f'\033[0;31mNão é um número válido!\033[m')
            else:
                break
        def_menu.cadastro('pessoas.txt', nome, idade)
        sleep(2)
    elif opcao == 3:
        def_menu.thau()
        sleep(2)
        break
