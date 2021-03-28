
import math

angulo = float(input('Digite um ãlgulo: '))
arad = math.radians(angulo)
print('O seno de {} é {:.2f}'.format(angulo, math.sin(arad)))
print('O cosseno de {} é {:.2f}'.format(angulo, math.cos(arad)))
print('A tangente de {} é {:.2f}'.format(angulo, math.tan(arad)))
