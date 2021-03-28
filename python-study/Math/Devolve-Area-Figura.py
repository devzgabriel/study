
pi = 3.14159
i = input().split()
A = float(i[0])
B = float(i[1])
C = float(i[2])
area_trinagulo = A * C / 2
area_circulo = pi * pow(C, 2)
area_trapezio = C * (A + B) / 2
area_quadrado = B * B
area_retangulo = A * B
print("TRIANGULO: {:.3f}".format(area_trinagulo))
print("CIRCULO: {:.3f}".format(area_circulo))
print("TRAPEZIO: {:.3f}".format(area_trapezio))
print("QUADRADO: {:.3f}".format(area_quadrado))
print("RETANGULO: {:.3f}".format(area_retangulo))
