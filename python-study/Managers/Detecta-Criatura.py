
p1 = input().strip()
if p1 == 'vertebrado':
    p2 = input().strip()
    if p2 == 'ave':
        p3 = input().strip()
        if p3 == 'carnivoro':
            print('aguia')
        elif p3 == 'onivoro':
            print('pomba')
    elif p2 == 'mamifero':
        p3 = input().strip()
        if p3 == 'onivoro':
            print('homem')
        elif p3 == 'herbivoro':
            print('vaca')
if p1 == 'invertebrado':
    p2 = input().strip()
    if p2 == 'inseto':
        p3 = input().strip()
        if p3 == 'hematofago':
            print('pulga')
        if p3 == 'herbivoro':
            print('lagarta')
    if p2 == 'anelideo':
        p3 = input().strip()
        if p3 == 'hematofago':
            print('sanguessuga')
        if p3 == 'onivoro':
            print('minhoca')
