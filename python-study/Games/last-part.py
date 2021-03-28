#jogo onde quer tirar a ultima peça perde
#Regras:
#É possivel escolher uma partida ou campeonato, e limite de peças por jogada
#Computador escolhe quem começa

def menu():
    print('Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato 2')
    modo=int(input())
    while 1 != modo!=2:
        print('Bem-vindo ao jogo do NIM! Escolha:\n\n1 - para jogar uma partida isolada\n2 - para jogar um campeonato 2')
        modo=int(input())
    if modo==1:
        print('Voce escolheu uma partida isolada!')
        partida()
    if modo==2:
        print('Voce escolheu um campeonato!')
        campeonato()


def partida():
    n = int(input('\nQuantas peças? '))
    m = int(input('Limite de peças por jogada? '))
    while n-m<0:
        print('Invalido')
        m = int(input('Limite de peças por jogada? '))                      #Dados sobre as pecas
    if n%(m+1)==0:
        print('\nVoce começa!')
        pecas_jog=usuario_escolhe_jogada(n,m)
        n-=pecas_jog
        vez='pc'
    else:
        print('\nComputador começa!')
        pecas_pc=computador_escolhe_jogada(n,m)
        n-=pecas_pc
        vez='jogador'                                                         #Escolhe quem comeca
    if n==1:
        print('Agora resta apenas uma peça no tabuleiro.')
    elif n>1:
        print(f'Agora restam {n} peças no tabuleiro.')                        #print nas Pecas restantes
    while n!=0:
        pecas=jogada(n,m,vez)
        n-=pecas
        if vez=='pc':
            vez='jogador'
        elif vez=='jogador':
            vez='pc'
        if n==1:
            print('Agora resta apenas uma peça no tabuleiro.')
        elif n>1:
            print(f'Agora restam {n} peças no tabuleiro.')            #alterna entre jogadores
    if vez=='jogador':
        print('Fim do jogo! O computador ganhou!')
        return 'pc'
    elif vez=='pc':
        print('Fim do jogo! Voce ganhou!')                            #print do Vencedor
        return 'jogador'


def computador_escolhe_jogada(n,m):
    pecas_pc=1
    while not (n-pecas_pc)%(m+1)==0:
        if pecas_pc<m:
            pecas_pc+=1
        elif pecas_pc==m:
            break
    if pecas_pc==1:
            print(f'\nO computador tirou uma peça.')
    else:
        print(f'\nO computador tirou {pecas_pc} peças.')
    return pecas_pc


def usuario_escolhe_jogada(n,m):
    if n>=m:
        pecas_jog=int(input('\nQuantas peças você vai tirar?'))
        while not 1<=pecas_jog<=m:
            print('\nOops! Jogada inválida! Tente de novo.')
            pecas_jog=int(input('\nQuantas peças você vai tirar?'))
            if pecas_jog==1:
                print(f'\nVocê tirou uma peça.')
            else:
                print(f'\nVocê tirou {pecas_jog} peças.')
        return pecas_jog


def jogada(n,m,vez):
    if vez=='pc':
        pecas = computador_escolhe_jogada(n,m)
    elif vez=='jogador':
        pecas = usuario_escolhe_jogada(n,m)
    return pecas


def campeonato():
    pc,jog=0,0
    for p in range(3):
        print(f'\n**** Rodada {p+1} ****')
        resultado=partida()
        if resultado=='pc':
            pc+=1
        elif resultado=='jogador':
            jog+=1
    print('**** Final do campeonato! ****')
    print(f'\nPlacar: Você {jog} X {pc} Computador')



menu()
