valor = int(input('Qual o Valor a ser Retirado'))
qtd_50 = qtd_20 = qtd_10 = qtd_1 = 0
while valor >= 50:
    qtd_50 += 1
    valor -= 50
while valor >= 20:
    qtd_20 += 1
    valor -= 20
while valor >= 10:
    qtd_10 += 1
    valor -= 10
while valor >= 1:
    qtd_1 += 1
    valor -= 1
print(
    f'São Necessáris {qtd_50} notas de R$ 50, {qtd_20} notas de R$ 20, {qtd_10} notas de R$ 10, {qtd_1} notas de R$ 1')

