seconds = int(input())
horas = 0
minute = 0
while True:
    if seconds >= 3600:
        seconds -= 3600
        horas += 1
    elif seconds >= 60:
        seconds -= 60
        minute += 1
    else:
        break
print("{}:{}:{}".format(horas, minute, seconds))

d = int(input())
anos = 0
meses = 0
while True:
    if d >= 365:
        d -= 365
        anos += 1
    elif d >= 30:
        d -= 30
        meses += 1
    else:
        break
print("{} ano(s)".format(anos))
print("{} mes(es)".format(meses))
print("{} dia(s)".format(d))