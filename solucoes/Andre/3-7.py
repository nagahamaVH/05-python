def min(vetor):
    m = vetor[0]
    for x in vetor:
        if x < m:
            m = x
    return m

def max(vetor):
    m = vetor[0]
    for x in vetor:
        if x > m:
            m = x
    return m

print(min([3,7,5,9,2,4,1,6]))
print(max([3,7,5,9,2,4,1,6]))
print(min(['a','t','d','n', 'í']))
print(max(['a','t','d','n', 'í']))

