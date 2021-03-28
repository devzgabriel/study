
from datetime import datetime

now = datetime.now()
data = int(input('Nacimento: '))
idade = now.year - data
if idade < 9:
    print('Mirim')
elif idade < 14:
    print('Infantil')
elif idade < 19:
    print('Junior')
elif idade < 20:
    print('Senior')
else:
    print('Master')
