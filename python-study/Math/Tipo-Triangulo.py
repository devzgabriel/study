i = input('Retas de triangulo:').split()
v = [float(i) for i in i]
v.sort(reverse=True)
a = v[0]
b = v[1]
c = v[2]
if a >= b + c:
    print('NAO FORMA TRIANGULO')
elif a ** 2 == b ** 2 + c ** 2:
    print('TRIANGULO RETANGULO')
elif a ** 2 > b ** 2 + c ** 2:
    print('TRIANGULO OBTUSANGULO')
elif a ** 2 < b ** 2 + c ** 2:
    print('TRIANGULO ACUTANGULO')
if a == b == c:
    print('TRIANGULO EQUILATERO')
elif a == b or b == c or a == b:
    print('TRIANGULO ISOSCELES')
