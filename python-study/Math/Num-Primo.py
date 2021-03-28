primo = int(input('Digite o número: '))
resultado = True
for n in range(2, primo):
    if primo % n == 0:
        resultado = False
if resultado == True:
    print('É um número primo')
else:
    print('Não é um número primo')
