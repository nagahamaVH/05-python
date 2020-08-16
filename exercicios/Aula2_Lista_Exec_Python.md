# Aula 2 - Exercícios Introdutórios em Python

Agora que já obtivemos certa experiência com a linguagem, vamos resolver alguns problemas um pouco mais complexos do comeco ao fim.

### 1) Escreva um programa que, dados 2 números diferentes (a e b), encontre o menor deles.

### 2) Para doar sangue é necessário:

* Ter entre 16 e 69 anos.
* Pesar mais de 50 kg.
* Estar descansado (ter dormido pelo menos 6 horas nas últimas 24 horas).

Faça um programa que pergunte a idade, o peso e quanto dormiu nas últimas 24 h para uma pessoa e diga se ela pode doar sangue ou não.

### 3) Considere uma equação do segundo grau f(x)=a⋅x2+b⋅x+c. A partir dos coeficientes, determine se a equação possui duas raízes reais, uma, ou se não possui.

### 4) Leia dois números e efetue a adição. Caso o valor somado seja maior que 20, este deverá ser apresentado somando-se a ele mais 8; caso o valor somado seja menor ou igual a 20, este deverá ser apresentado subtraindo-se 5.

### 5) Leia um número e imprima a raiz quadrada do número caso ele seja positivo ou igual a zero e o quadrado do número caso ele seja negativo.

### 6) Escreva uma funcão para verificar a velocidade de motoristas. Essa funcão deve ter um parametro: `speed`.
    1.  Se speed menor que 70, deve imprimir “Ok”.
    2.  Case contrário, para cada 5km/h acima do limite (70), o radar deve aplicar um ponto na carteira do motorista, imprimindo quantos pontos foram retirados. Por exemplo, se speed é 80, Deve imprimir: “Pontos: 2”.
    3.  Se o motorista tomar mais que 12 pontos, a funcão deve imprimir: “Licen suspended”

### 7) Leia um número inteiro entre 1 e 12 e escreva o mês correspondente. Caso o usuário digite um número fora desse intervalo, deverá aparecer uma mensagem informando que não existe mês com este número.

### 8)  Escreva uma funcão `show_stars(rows)`. Se `rows` for 5, deve-se imprimir o seguinte:
    ```
    *
    **
    ***
    ****
    *****
    ```


### 9)  Escreva uma funcão chamada `showNumbers`, que recebe o parâmetro `limit.` A funcão deve imprimir todos os números entre 0 e limit com uma label para identificar se o número é par ou ímparPor exemplo, se o limite for 3, deve-se imprimir:
    *   0 PAR
    *   1 IMPAR
    *   2 PAR
    *   3 IMPAR

### 10) Escreva uma funcào que retorna a soma de múltiplos de 3 e 5 entre 0 e `limit` (parâmetro). Por exemplo, se limite for 20, deve retornar a soma de 3, 5, 6, 9, 10, 12, 15, 18, 20.

### 11) Escreva uma funcão que imprima todos os números primos entre 0 e `limit` (um parâmetro).

### 12) O python tem uma implementacão padrão de uma funcão ``sum`` para achar a soma dos elementos de uma lista, faca sua própria implementacão da funcão
```

    >>> sum([1, 2, 3])
    >>> 6
```

### 13) O que acontece quando a sua funcão ``sum`` é chamaca com uma lista de strings? Voce consegue fazer a sua funcao funcionar com strings também?

```

    >>> sum(["hello", "world"])
    "helloworld"
    >>> sum(["aa", "bb", "cc"])
    "aabbcc"
```
### 14): Implemente uma funcão ``product``, para computar o produto de uma lista de números.

```

    >>> product([1, 2, 3])
    6
```

### 15) Implemente uma funcão que calcula o fatorial de um número:

```

    >>> factorial(4)
    24
```

### 16) Escreva um programa ``reverse.py`` para imprimir linhas de um arquivo na ordem inversa.

``` 
      $ cat she.txt
      She sells seashells on the seashore;
      The shells that she sells are seashells I'm sure.
      So if she sells seashells on the seashore,
      I'm sure that the shells are seashore shells.

      $ python reverse.py she.txt
      I'm sure that the shells are seashore shells.
      So if she sells seashells on the seashore,
      The shells that she sells are seashells I'm sure.
      She sells seashells on the seashore;
```

### 17) Escreva um programa `wrap.py` que recebe o nome de um arquivo e um comprimento, e quebra as linhas com comprimento maior que o argumento.

```
    $ python wrap.py she.txt 30
    I'm sure that the shells are s
    eashore shells.
    So if she sells seashells on t
    he seashore,
    The shells that she sells are 
    seashells I'm sure.
    She sells seashells on the sea
    shore;
```


### 18) Escreva um programa que conta a frequência de cada caracter em um arquivo.



### 19) Escreva um programa que acha os anagramas em uma lista de palavras (duas palavras são anagramas se uma palavra pode ser formada rearranjando as letras de outra)  

```

    >>> anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
    [['eat', 'ate', 'tea], ['done', 'node'], ['soup']]
```    
### 20) Escreva uma funcão ``valuesort`` para ordenar valores em um dicionário baseado em sua chave.

```

    >>> valuesort({'x': 1, 'y': 2, 'a': 3})
    [3, 1, 2]
```
### 21) Escreva a funcão ``invertdict`` para inverter chaves e valores no dicionário.

```

    >>> invertdict({'x': 1, 'y': 2, 'z': 3})
    {1: 'x', 2: 'y', 3: 'z'}
```
