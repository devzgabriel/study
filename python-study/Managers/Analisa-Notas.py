def notas(n):
    diario = {'Quantidade de notas': len(n), 'Maior nota': max(n), 'Menor nota': min(n)}
    for s in n:
        t = 0
        t += s
    t = t / len(n)
    diario['Média'] = t
    if t >= 6:
        diario['Situação'] = 'Boa'
    else:
        diario['Situação'] = 'Ruim'
    return diario


print(notas([2, 4, 3, 7, 6, 8, 6, 9, 7, 90]))