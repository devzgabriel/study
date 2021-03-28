import random
randon_list = []
for n in range(5):
    randon_list.append(random.randrange(1, 15))
print(randon_list)
print(f'Maior:{max(randon_list)}')
print(f'Menor:{min(randon_list)}')
