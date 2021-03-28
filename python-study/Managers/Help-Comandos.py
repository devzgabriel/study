def perg():
    print('\33[7:33m-=' * 15)
    print(f'\33[7:33m Qual comando quer aprender[FIM para sair]:')
    print('\33[7:33m-=' * 15)
    comando = str(input('\33[m'))
    if comando.upper != 'FIM':
        print(f'\33[7:34m')
        print(help(comando))
        print(f'\33[m')
    else:
        return 'FIM'


while True:
    if perg() == 'FIM':
        break
