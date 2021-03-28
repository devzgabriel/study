
from datetime import datetime

trab = {'Nome': input('Nome: '), 'Nascimento': int(input('Nascimento: ')),
        'Carteira': int(input('Carteira(0=não tem): '))}
trab['Idade'] = datetime.now().year - trab["Nascimento"]
if trab['Carteira'] != 0:
    trab['Ano de contratação'] = int(input('Ano de contratação: '))
    trab['Salário'] = float(input('Salário: '))
    trab['Aposetadoria'] = trab["Idade"] + (trab["Ano de contratação"] + 35) - datetime.now().year
print('-=' * 20)
for k, v in trab.items():
    print(f' > {k} ----- {v}')
