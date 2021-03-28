def aumentar(v=0, p=0):
    v = v + (v * (p / 100))
    return v


def reduzir(v=0, p=0):
    v = v - (v * (p / 100))
    return v


def dobro(v=0):
    v *= 2
    return v


def metade(v=0):
    v /= 2
    return v


def dinheiro(v=0, moeda='R$ '):
    return f'{moeda}{v.replace(".", ",")}'
