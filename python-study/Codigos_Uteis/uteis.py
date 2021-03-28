#------------------------------------------------------primos
n=int(input('Digite um número inteiro: '))
fator=2
while fator!=n:
    if n%fator==0:
        bprimo=False
        break
    else:
        bprimo=True
    fator+=1
if bprimo:
    print('primo')
else:
    print('não primo')


#------------------------------------------------------numeros em sequência 

i=input('Digite um número inteiro: ')
a=0
while a<len(i)-1:
    if i[a] in i[a+1]:
        adj=True
        break
    else:
        adj=False
    a+=1
if adj:
    print('sim')
else:
    print('não')

#------------------------------------------------------maior primo
def maior_primo(n):
    r=True
    while r:
        c=2
        while c!=n:
            if n%c==0:
                bprimo=False
                break
            else:
                bprimo=True
            c+=1
        if bprimo:
            print (n)
            r=False
        else:
            n-=1

#------------------------------------------------------fatorial
n = int(input('Digite o valor de n: '))
fn= 1
if n==0:
    print(1)
else:
    while n> 1:
        fn= n*fn
        n-=1
    print(fn)


#------------------------------------------------------fatoraçao
n=int(input('Digite um número: '))

fator=2
exp=0
while n>1:
    while n% fator==0:
        n/=fator
        exp+=1
    if exp>0:
        print(f'Fator {fator} com exp: {exp}')
    fator+=1
    exp=0


#------------------------------------------------------soma hipotenusas entre 1 e n
def é_hipotenusa(h):
    for i in range(1,h+1):
        for j in range(1,h+1):
            if (i*i) + (j*j) == (h*h):
                return True
    return False

def soma_hipotenusas(n):
    soma=0
    h=1
    while h <= n:
        if é_hipotenusa(h):
            soma+=h
        h+=1
    return soma