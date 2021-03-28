
i = input().split()
hora_inicio = int(i[0])
min_inicio = int(i[1])
hora_final = int(i[2])
min_final = int(i[3])
hora_total = hora_final - hora_inicio
if hora_total < 0:
    hora_total += 24
min_total = min_final - min_inicio
if min_total < 0:
    min_total += 60
    hora_total -= 1
if min_total == 0 and hora_total == 0:
    print('O JOGO DUROU 24 HORA(S) E 0 MINUTO(S)')
else:
    print('O JOGO DUROU {} HORA(S) E {} MINUTO(S)'.format(hora_total, min_total))
