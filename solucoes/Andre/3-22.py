import sys
#print "This is the name of the script: ", sys.argv[0]
#print "Number of arguments: ", len(sys.argv)
#print "The arguments are: " , str(sys.argv)
a = open(sys.argv[1])
compr = int(sys.argv[2])

a_wrap = []
for x in a:
    if len(x) <= compr:
        a_wrap.append(x)
    else:
        while len(x) > compr:
            a_wrap.append(x[:compr])
            x = x[compr:]
        a_wrap.append(x)

for x in a_wrap:
    print(x)
