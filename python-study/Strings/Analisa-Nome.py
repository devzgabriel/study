
nome = str(input('Qual o nome?')).strip()
print('Tem Silva? {}'.format("SILVA" in nome.upper()))
cortado = nome.split()
print('Seu primeiro nome é: {} e o último é: {}'.format(cortado[0], cortado[len(cortado) - 1]))


frase = str(input('Qual a frase? ')).upper().strip()
print('A letra A aparece{} vezes'.format(frase.count('A')))
print('Ela parece pela primeira vez na {} casa'.format(frase.find('A') + 1))
print('Ela parece pela última vez na {} casa'.format(frase.rfind('A') + 1))