
def analisa_numero(lista):
    null = 0
    even = []
    odd = []
    positive = []
    negative = []
    for i in lista:
        if i == 0:
            print('NULL')
            null += 1
        elif i != 0 and i % 2 == 0:
            print('EVEN', end=' ')
            even.append(i)
        elif i != 0 and i % 2 != 0:
            print('ODD', end=' ')
            odd.append(i)
        if i > 0:
            print('POSITIVE')
            positive.append(i)
        elif i < 0:
            print('NEGATIVE')
            negative.append(i)
    return {null, even, odd, positive, negative}
