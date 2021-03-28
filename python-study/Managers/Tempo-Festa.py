
di = input().split()
di = int(di[1])
hi = input().split(' : ')
dt = input().split()
dt = int(dt[1])
ht = input().split(' : ')
hi = [int(n) for n in hi]
ht = [int(n) for n in ht]

d = dt - di
if d < 0:
    d += 30
h = ht[0] - hi[0]
if h < 0:
    h += 24
    d -= 1
m = ht[1] - hi[1]
if m < 0:
    m += 60
    h -= 1
s = ht[2] - hi[2]
if s < 0:
    s += 60
    m -= 1
print('{} dia(s)'.format(d))
print('{} hora(s)'.format(h))
print('{} minuto(s)'.format(m))
print('{} segundo(s)'.format(s))
