## Criando um pacote

Arquivo python textFunctions.py
```
def SayHello(name):
    print("Hello " + name)
    return
    
def repeatString(str,num):
    print(str*num)
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

app2.py
```
from package.functions import sum
sum(3,2)
power(3,2)
```

app3.py
```
from package import textFunctions
textFunctions.SayHello("a")
textFunctions.repeatString("abc",3)
```
## Instalado pacotes no ambiente conda

Definindo arquivo setup.py

```
from setuptools import setup
setup(name='package',
version='0.1',
description='Testing installation of Package',
url='#',
author='Silvio',
author_email='silvio.stanzani@sprace.org.br',
license='N/D',
packages=['package'],
install_requires=[
          'pandas',
      ],
zip_safe=False)
```

Instalado pacote no ambiente conda

```
pip install . --user
```
