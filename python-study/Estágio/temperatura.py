import math

t = 0
c = 0
n = int(input())
lista=input().split()
while c < n:
    if c == 0:
        t = int(lista[c])
    elif abs(int(lista[c])) < abs(t):
        t = int(lista[c])
    elif abs(int(lista[c])) == abs(t):
        if int(lista[c]) >= t:
            t = int(lista[c])
    c += 1
print(t)
