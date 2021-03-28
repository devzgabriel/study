valores = []
for n in range(100):
    valores.append(int(input()))
    if n == 1 or valores[len(valores) - 1] == max(valores):
        maior = valores[len(valores) - 1]
        posicao = len(valores)
print(maior)
print(posicao)
