aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = int(input(f'Média de {aluno["nome"]}: '))
if aluno["media"] >= 7:
    situacao = 'Aprovado'
else:
    situacao = 'Reprovado'
print(f'{aluno["nome"]} com média {aluno["media"]} está {situacao}')
