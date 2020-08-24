list=int(input("Insira numeros separados por um espaço: ").split())
def product(list):
    p = 1
    for i in list:
        p *= i
    return p
product(list)
