import math

forcas=[]
n = int(input())

for i in range(n):
    pi = int(input())
    forcas.append(pi)

forcas.sort()
menor_d=forcas[0]
for i in range(len(forcas)-1):
    d=forcas[i+1] - forcas[i]
    if d < menor_d:
        menor_d = d
print(menor_d)


'''
import sys
import math

t=0
n = int(input())
for e,i in enumerate(input().split()):
    if (int(i)==0) or (e==0):
        t = int(i)
    elif (abs(int(i))-ref)<0:
        t=int(i)
    ref=abs(t)
print(t)


'''


'''ultimo=len(forcas)-1
menor_d=0

for i in range(len(forcas)-1):
    diferenca = forcas[ultimo]-forcas[ultimo-1]
    if i == 0:
        menor_d=diferenca
    elif diferenca<menor_d:
        menor_d=diferenca
    ultimo = ultimo-1
print(menor_d)'''