string_1 = input("Digite a primeira string: ")
string_2 = input("Digite a segunda string: ")

cont = 0
nivel = 0
for a in sorted(string_1):
    if(a == sorted(string_1)[cont]):
        nivel += 1
    cont += 1

print(nivel)

if(string_1 == string_2):
    print("São strings idênticas")
else:
    print("Não são strings idênticas")
