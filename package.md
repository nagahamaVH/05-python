## Criando um pacote

Arquivo python greet.py
```
def SayHello(name):
    print("Hello " + name)
    return
```

Arquivo python functions.py
```
def sum(x,y):
    return x+y

def average(x,y):
    return (x+y)/2

def power(x,y):
    return x**y
```

O nome do pacote é o nome da pasta na qual os arquivos estão armazenados

Para que o diretório seja definido com um pacote, deve conter um arquivo python com o seguinte nome: \_\_init\_\_.py 

O diretório de pacote ficará na seguintes pasta: ~/myapp/package

O diretório da aplicação ficará na seguintes pasta: ~/myapp/

app.py
```
from package import functions
functions.power(3,2)
```
