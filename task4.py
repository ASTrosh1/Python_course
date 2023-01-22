dct = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
def mem(d):
    newdct = dict()
    for k,v in d.items():
        if v >= 3:
            newdct[k]=d[k]
    return newdct

print(mem(dct))