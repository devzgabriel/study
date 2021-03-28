def remove_repetidos(lst):
    new_l=[]
    for o in lst:
        if o not in new_l:
            new_l.append(o)
    new_l.sort()
    return new_l
