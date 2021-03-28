
def analisa_quadrante(x, y):
    if x == 0:
        if y == 0:
            print('Origem')
        else:
            print('Eixo Y')
    elif y == 0 and x != 0:
        print('Eixo X')
    elif x > 0:
        if y > 0:
            print('Q1')
        if y < 0:
            print('Q4')
    elif x < 0:
        if y > 0:
            print('Q2')
        if y < 0:
            print('Q3')
