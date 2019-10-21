import re

class ExercicioOop :
    def __init__(self,texto):
        self.texto = ''
        i = 0
        while i < len(texto):
            if texto[i] == '\n':
                self.texto += texto[:i]
                texto = texto[i+1:]
                i = 0
            else:
                i += 1
        self.texto += texto
        self.palavras = re.sub("[^\w]", " ", self.texto).split()
        self.frequencia = {}
        self.stop_words = []

    def contar_frequencia(self):
        for p in self.palavras:
            if p not in self.frequencia:
                self.frequencia[p] = 1
            elif p not in self.stop_words:
                self.frequencia[p] += 1
    
    def top_10(self):
        aux = sorted(self.frequencia.items(), key=lambda x: x[1], reverse = True)
        top = []

        for i in range(10):
            top.append(aux[i][0])
        
        return top

    def media(self):
        soma_f = 0
        for f in self.frequencia.values():
            soma_f += f
        print(soma_f,len(self.frequencia))
        
        return soma_f/len(self.frequencia)
                
    def desvio_padrão(self):
        print("fazer depois")
    
    def cadastrar_stop_words(self, lista):
        self.stop_words = lista

    def remover_stop_words(self):
        aux = re.findall(r"[\w]+|[^\w]" , self.texto)
        texto_limpo  = ""

        for p in aux:
            if p not in self.stop_words:
                texto_limpo += p 

        return texto_limpo


    def continuar(self):
        print("Continuar depois blz?")

f = open("t8.shakespeare.txt", "r")
e = ExercicioOop(f.read())
#print(e.palavras)
e.contar_frequencia()
print(e.frequencia)
print(e.top_10())
print(e.media())
e.cadastrar_stop_words(["the", "I", "and", "to", "of", "a", "my", "in", "d"])
print(e.stop_words)
print(e.remover_stop_words())
e.contar_frequencia()
print(e.frequencia)
print(e.top_10())
print(e.media())
print(e.stop_words)