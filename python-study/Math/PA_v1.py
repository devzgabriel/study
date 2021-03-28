prim_term = int(input('Qual o Primeiro termo: '))
razao = int(input('Qual a Razão: '))
term = int(input('Quantos termos quer saber: '))
ultimo_term = prim_term + (term)*razao
for c in range(prim_term, ultimo_term, razao):
    print(f'{c}', end=',')
