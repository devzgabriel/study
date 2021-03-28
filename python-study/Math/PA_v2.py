prim_term = int(input('Qual o Primeiro termo: '))
razao = int(input('Qual a Razão: '))
n_term = int(input('Quantos termos quer saber: '))
term = prim_term
c = 0
mais = 1
while mais != 0:
    n_term += mais
    while c < n_term:
        print(term, end='')
        print(','if c+1 < n_term else '', end='')
        term += razao
        c += 1
    mais = int(input('\n\n Quer mostrar quantos termos a mais? '))
print('Fim')
