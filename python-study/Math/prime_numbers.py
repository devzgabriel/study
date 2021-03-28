#Descubra se é um primo e quantos primos há entre 0 e ele


def primo(n):
    fator=2
    while fator!=n:
        if n%fator==0:
            return False
        fator+=1
    return True


def n_primos(n):
    qtd=0
    if n>=2:
        a=2
        while a<=n:
            if primo(a):
                qtd+=1
            a+=1
    return qtd

n = int(input('Qual o número máximo para descobrir seus primos menores'))
print(f"Há {n_primos(n)} entre 1 e {n}.")
print(f"(Primo: {primo(n)})")
