dicionario = {
    'x': 1,
    'y': 2,
    'a': 3,
}

def valueSort(dicionario):
    sortedDict = sorted(dicionario.items())
    sortedValues = [n[1] for n in sortedDict]
    return sortedValues

print (valueSort(dicionario))