def menu(opc):
    print('!*!' * 10)
    print(f'{"Menu de Cadastro":^30}')
    c = 1
    for item in opc:
        print(f'\033[33m{c}\033[m - \033[34m{item}\033[m')
        c += 1
    print('!*!' * 10)
    # -------------------------------------------------------------Validação de opcão
    while True:
        opcao = input('Sua Opção: ').strip()
        if opcao.isnumeric():
            opcao = int(opcao)
            if 1 <= opcao <= 3:
                return opcao
            else:
                print(f'\033[0;31mNão é uma opção válida!\033[m')
        else:
            print(f'\033[0;31mNão é um número válido!\033[m')


def verlista(arq):
    try:
        a = open(arq, "rt+")
    except FileNotFoundError:
        a = open(arq, 'wt+')
    finally:
        for l in a:
            dado = l.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30}{dado[1]:>3} anos')
        a.close()


def cadastro(arq, nome, idade):
    try:
        a = open(arq, 'at')
    except:
        print('Erro ao Manipular Arquivo')
    else:
        try:
            a.write(f'{nome};{idade}\n')
            a.close()
            print('Usuário cadastrado')
        except:
            print('Erro ao cadastrar usuário')


def thau():
    print('!*!' * 10)
    print(f'\033[32m{"VOLTE SEMPRE":^30}\033[m')
    print('!*!' * 10)
