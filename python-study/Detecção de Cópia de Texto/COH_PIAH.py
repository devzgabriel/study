'''
O objetivo é detectar quem está copiando o texto baseando nos tracos linguisticos de cada texto
'''


import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")

    wal = float(input("Entre o tamanho medio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    somatoria = 0
    for c in range(6):
        somatoria += abs((as_a[c]) - (as_b[c]))
    somatoria/=6
    return somatoria

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    qtd_letras = 0
    for c in texto:
        if ' ' in c:
            qtd_letras+=1
    sentencas = separa_sentencas(texto)
    frases = []
    palavras = []
    for s in sentencas:
        auxiliar = separa_frases(s)
        for a in auxiliar:
            frases.append(a)
    for f in frases:
        auxiliar = separa_palavras(f)
        for a in auxiliar:
            palavras.append(a)
    qtd_sentencas = len(sentencas)
    qtd_frases = len(frases)
    qtd_palavras = len(palavras)
    for p in palavras:
        qtd_letras += len(p)
    wal_aux = qtd_letras/qtd_palavras
    ttr_aux = n_palavras_diferentes(palavras)/qtd_palavras
    hlr_aux = n_palavras_unicas(palavras)/qtd_palavras
    sal_aux = qtd_letras/qtd_sentencas
    sac_aux = qtd_frases/qtd_sentencas
    pal_aux = qtd_letras/qtd_frases
    '''print(qtd_sentencas)
    print(qtd_frases)
    print(qtd_palavras)
    print(qtd_letras)
    print(sentencas)
    print(frases)
    print(palavras)
    print([wal_aux,ttr_aux,hlr_aux,sal_aux,sac_aux,pal_aux])'''
    as_b = [wal_aux,ttr_aux,hlr_aux,sal_aux,sac_aux,pal_aux]
    return as_b

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    lista_grau_similaridade = []
    for t in textos:
        as_b = calcula_assinatura(t)
        lista_grau_similaridade.append(compara_assinatura(ass_cp,as_b))
    infectado = lista_grau_similaridade.index(min(lista_grau_similaridade)) + 1
    return infectado



''' Tamanho médio de palavra: Média simples do número de caracteres por palavra.
    Relação Type-Token: Número de palavras diferentes utilizadas em um texto divididas pelo total de palavras.
    Razão Hapax Legomana: Número de palavras utilizadas uma vez dividido pelo número total de palavras.
    Tamanho médio de sentença: Média simples do número de caracteres por sentença.
    Complexidade de sentença: Média simples do número de frases por sentença.
    Tamanho médio de frase: Média simples do número de caracteres por frase.



    ========================================Programa Principal========================================'''

#calcula_assinatura('Muito além, nos confins inexplorados da região mais brega da Borda Ocidental desta Galáxia, há um pequeno sol amarelo e esquecido. Girando em torno deste sol, a uma distancia de cerca de 148 milhões de quilômetros, há um planetinha verde-azulado absolutamente insignificante, cujas formas de vida, descendentes de primatas, são tão extraordinariamente primitivas que ainda acham que relógios digitais são uma grande ideia.')

infectado = avalia_textos(le_textos(),le_assinatura)
print(f'O autor do texto {infectado} está infectado com COH-PIAH')
