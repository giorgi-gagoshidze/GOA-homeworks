def distinct(seq):
    h=[]
    for i in seq:
        if i not in h:
            h.append(i)
    return h