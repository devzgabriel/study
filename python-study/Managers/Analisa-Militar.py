from datetime import date

atual = date.today().year
nasc = int(input('Data de nascimento: '))
idade = atual - nasc
if idade == 18:
    print('Está na hora de alistar')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o alistamento em {}'.format(saldo, atual + saldo))
elif idade > 18:
    saldo = idade - 18
    print('Já passou {} anos do alistamento em {}'.format(saldo, atual - saldo))
