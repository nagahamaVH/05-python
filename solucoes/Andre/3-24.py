import sys

a = open(sys.argv[1]).readlines()

a_center = []
compr = 0
for x in a:
    if len(x) > compr:
        compr = len(x)
for x in a:
    a_center.append(int((compr-len(x))/2) * " " + x)

for x in a_center:
    print(x)

