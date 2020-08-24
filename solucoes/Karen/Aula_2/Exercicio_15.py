#!/usr/bin/python3

def funcao_fatorial(limit):
        fatorial = 1
        for i in range(1,limit+1):
                fatorial = i*fatorial
        print (fatorial)  

f = funcao_fatorial(5)   

