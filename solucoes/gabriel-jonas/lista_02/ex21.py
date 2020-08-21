dicionario = {
    'x': 1,
    'y': 2,
    'z': 3,
}

def invertDict(dictionary):
    invDict = {}
    for i in dicionario.items():
        invDict[i[1]] = i[0]
    return invDict

print (invertDict(dicionario))

