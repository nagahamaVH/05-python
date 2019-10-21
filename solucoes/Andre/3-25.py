def zip(v1, v2):
    return [tuple([v1[i],v2[i]]) for i in range(len(v1))]

print(zip([1,2,3], ["a", "b", "c"]))
