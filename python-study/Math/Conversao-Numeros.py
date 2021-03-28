num = int(input('Número: '))
base = int(input('escolha a base de conversão \n1-BINÁRIO \n2-OCTAL \n3-HEXADECIMAL'))
if base == 1:
    print('{} convertido em Binário é {}'.format(num, bin(num)[2:]))
elif base == 2:
    print('{} convertido em Octal é {}'.format(num, oct(num)[2:]))
elif base == 3:
    print('{} convertido em HEXADECIMAL é {}'.format(num, hex(num)[2:]))
else:
    print('opção invalida')
