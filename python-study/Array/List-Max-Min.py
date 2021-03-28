val_max_min = []
for p in range(0, 5):
    val_max_min.append(input(f'Digite um valor para posição {p}'))
print(f'O maior valor digitado:{max(val_max_min)} na posição: ', end='')
for p, v in enumerate(val_max_min):
    if v == max(val_max_min):
        print(f'{p}')
print(f'O menor valor digitado:{min(val_max_min)} na posição: ', end='')
for p, v in enumerate(val_max_min):
    if v == min(val_max_min):
        print(f'{p}')
