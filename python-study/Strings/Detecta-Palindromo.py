frase = str(input('Digite uma frase: ')).strip().lower()
junto = ''.join(frase.split())
inverso = ''
for letra in range(len(junto) - 1, -1, -1):
    inverso = inverso + junto[letra]
print(inverso)
if inverso == junto:
    print('É um palindromo')
else:
    print('Não é um palindromo')
