n_idade = 0
n_hom = 0
n_mul = 0
gen = '42'
contin = '42'
while True:
    idade = int(input('Digite a Idade da pessoa: '))
    while gen not in 'MmFf':
        gen = input('Digite seu Genero[M/F]: ').upper()
    while contin not in 'SsNn':
        contin = input('Continuar?[S/N]')
    if idade >= 18:
        n_idade += 1
    if gen == 'M':
        n_hom += 1
    if idade < 20 and gen == 'F':
        n_mul += 1
    if contin in 'Nn':
        break
    gen = '42'
    contin = '42'
print(f'Há {n_idade} pessoas com mais de 18 anos, {n_hom} homens e {n_mul} mulheres com menos de 20 anos.')
