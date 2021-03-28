valor = float(input())
notas = [100, 50, 20, 10, 5, 2]
moedas = [1, 0.50, 0.25, 0.10, 0.05, 0.01]
print('NOTAS:')
for nota in notas:
    qtd_notas = int(valor / nota)
    print("{} nota(s) de R$ {:.2f}".format(qtd_notas, nota))
    valor -= qtd_notas * nota
print('MOEDAS:')
for moeda in moedas:
    qtd_moeda = int(round(valor, 2) / moeda)
    print("{} moeda(s) de R$ {:.2f}".format(qtd_moeda, moeda))
    valor -= qtd_moeda * moeda
