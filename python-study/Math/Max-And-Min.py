prin = int(input('primeiro numero: '))
segn = int(input('segundo numero: '))
tern = int(input('terceiro numero: '))
if prin > segn and prin > tern:
    print('o maior número é: ', prin)
if segn > prin and segn > tern:
    print('o maior número é: ', segn)
if tern > prin and tern > segn:
    print('o maior número é: ', tern)
if prin < segn and prin < tern:
    print('o menor número é: ', prin)
if segn < prin and segn < tern:
    print('o menor número é: ', segn)
if tern < prin and tern < segn:
    print('o menor número é: ', tern)
