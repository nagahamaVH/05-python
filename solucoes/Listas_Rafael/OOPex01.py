# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

# Ex OOP
import textdistance

# Inicializa a classe  
class ManipulaTXT:
    # Método construtor recebendo o arquivo como parâmetro
    def __init__(self, arquivo):
        self.arquivo = open(arquivo, "r")
        self.lista = [lines.strip("\n").split(" ") for lines in self.arquivo]
        self.words = []
        self.libword = {}
        self.popular = []
        self.stopwords = []
        self.novotexto = ""
    # Método para retornar o texto com uma lista de strings    
    def returnlista(self):
        return self.lista
    # Método para retornar cada palavra do texto
    def singleword(self):
        for i in range(len(self.lista)):
            for j in range(len(self.lista[i])):
                self.words.append(self.lista[i][j])
                #print(self.lista[i][j])
        return self.words
    # Método para contar a freq de cada palavra
    def histogramawords(self):
        self.libword = {}
        for i in self.words:
            if i in self.libword:
                self.libword[i] += 1
            else:
                self.libword[i] = 1
        return self.libword
    # Método para retornar as 10 palavras mais frequentes
    def mostpopular(self):
        self.popular = sorted((keyy, valuee) for (valuee, keyy) in self.libword.items())
        return self.popular[-10:][::-1]
    # Média e desvio padrão
    def mediadesvio(self):
        self.keys = [i for i in self.libword]
        self.keys.sort()
        self.media = [self.libword[i] for i in self.keys]
        self.media = sum(self.media)/len(self.media)
        print("A média é: ", self.media)
        self.desvio = (sum((self.libword[i]-self.media)**2 for i in self.keys)/len(self.keys))**(1/2)
        print("O desvio é: ", self.desvio)
    # Cadastrar stopwords
    def newSW(self, stop):
        self.stopwords.append(stop)
        return self.stopwords
    # Retorna texto eliminando as stopwords
    def textosemSW(self):
        for i in self.words:
            if not i in self.stopwords:
                self.novotexto += i + " "
        return self.novotexto        
    # Similaridade palavras
    def txtdist(self, w1, w2):
        return textdistance.levenshtein.normalized_similarity(w1, w2)

arqv001 = ManipulaTXT("exoo.txt")
arqv001.returnlista()
arqv001.singleword()
arqv001.histogramawords()
arqv001.mostpopular()
arqv001.mediadesvio()
arqv001.newSW("of")
arqv001.newSW("a")
arqv001.newSW("to")
arqv001.newSW("and")
arqv001.newSW("for")
arqv001.newSW("by")
arqv001.newSW("the")
arqv001.newSW("at")
arqv001.newSW("is")
arqv001.textosemSW()
print(arqv001.txtdist("arrow", "arow"))
