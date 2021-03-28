i = input().split()
A = float(i[0])
B = float(i[1])
C = float(i[2])
d = B ** 2 - 4 * A * C
if d >= 0 and A != 0:
    r1 = (-B + (d ** (1 / 2))) / (2 * A)
    r2 = (-B - (d ** (1 / 2))) / (2 * A)
    print("R1 = {:.5f}".format(r1))
    print("R2 = {:.5f}".format(r2))
else:
    print('Impossivel calcular')