def is_isogram(string):
    if len(string)==0:
        return True
    else:
        string = string.lower()
        r = True
        for l in range(len(string)):
            for c in string[l+1:]:
                if string[l]==c:
                    r = False
        return r
