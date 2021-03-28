palavra = str(input('Qual a palavra: '))
print('\nAs vogais são:')
for l in palavra:
    if l.lower() in 'aeiou':
        print(l, end='  ')
