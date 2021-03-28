print('PLANILHA DE ALUNOS')
planilha = []
while True:
    nome = str(input('Nome do aluno:'))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    media = (nota1 + nota2) / 2
    planilha.append([nome, [nota1, nota2], media])
    contin = input('Continuar a cadastrar?[S/N]').upper()
    while contin not in 'SN':
        contin = input('Continuar a cadastrar?[S/N]').upper()
    if contin == 'N':
        break
print(f'{"Núm":<5}{"Nome":^10}{"Média":>10}')
for n, a in enumerate(planilha):
    print(f'{n+1:<5}{a[0]:^10}{a[2]:>10}')
print()
while True:
    aluno = int(input('Abrir dados de Qual Aluno?[000=cancelar]')) - 1
    if aluno == 000:
        break
    elif 0 < aluno <= len(planilha):
        print(f'O Aluno {planilha[aluno][0]} com Média {planilha[aluno][2]} '
              f'teve as notas: {planilha[aluno][1][0]} e {planilha[aluno][1][1]}')
    else:
        print('Aluno Inválido')
print()
