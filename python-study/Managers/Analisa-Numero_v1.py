nm = []
par = 0
pos = 0
neg = 0
for n in range(5):
    nm.append(float(input()))
for n in nm:
    if n % 2 == 0:
        par += 1
    if n > 0:
        pos += 1
    elif n < 0:
        neg += 1
print('{} valor(es) par(es)'.format(par))
print('{} valor(es) impar(es)'.format(5 - par))
print('{} valor(es) positivo(s)'.format(pos))
print('{} valor(es) negativo(s)'.format(neg))
