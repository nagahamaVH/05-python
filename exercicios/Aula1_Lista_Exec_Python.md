# Aula 1 - Exercícios Introdutórios em Python

Os exercícios desta aula têm por objetivo prover familiaridade com os comandos básicos da linguagem de programacão Python, que serão essenciais no decorrer desta residência.
​
## Utilizando o interpretador Python
​
​
**1) :** Abra um novo interpretador Python e use-o para computar o valor da expressão ``2 + 3``.
​
## Executando Scripts Python

O interpretador Python geralmente não é diretamente utilizado para codificacão, mas pode ser utilizado para testar a instalacão ou para executar scripts pré-programados. Para os próximos exercícios, crie um script (extensão ``.py``) e o execute a partir do interpretador ou a sua IDE de preferência.


​
**2): ** Crie um script Python que imprime na tela  ``hello, world!`` quatro vezes.
​
**3): ** Crie um script python com o seguinte conteúdo e veja a saída:
​
\```
​
    1 + 2
\```

Se nada for impresso, o que você precisa mudar no código para que a resposta da expressão seja impressa?
​
## Exercícios

Para os próximos exercícios, tente descobrir a saída do programa sem rodá-lo. Então, execute o código e verifique se a saída é essa mesmo.

​
**4):**
​
```
​
    x = 4
    y = x + 1
    x = 2
    print(x, y)
```
**5):** 
​
```
​
    x, y = 2, 6
    x, y = y, x + 2
    print(x, y)
```
**6):** 
​
```
​
    a, b = 2, 3
    c, b = a, c + 1
    print(a, b, c)
​
```
## Funcões
​
**7):** Quantas multiplicacões são executadas quando cada uma das linhas de código são executadas?​
```
numcalls = 0
def square(x):
    global numcalls
    numcalls = numcalls + 1
    return x * x

print(square(5))
print(square(2*5))
```

**8):** Qual será a saída dos próximos programas?
​
```
​
	x = 1
	def f():
            return x
	print(x)
	print(f())
```
**9):** 
​
```
​
	x = 1
	def f():
            x = 2
            return x
	print(x)
	print(f())
	print(x)
```
**10):** 
​
```
​
	x = 1
	def f():
		y = x
		x = 2
		return x + y
	print(x)
	print(f())
	print(x)
```
**11):** 
​
```
​
    x = 2
    def f(a):
        x = a * a
        return x
    y = f(3)
    print(x, y)
```
**12):** Escreva a funcão ``count_digits`` que retorna quantos dígitos um número tem.
```
    >>> count_digits(5)
    1
    >>> count_digits(12345)
    5
```
**13): ** Escreva uma funcão `istrcmp` para comparar duas strings, ignorand se as letras são maiúsculas ou minúsculas.
​
```
​
    >>> istrcmp('python', 'Python')
    True
    >>> istrcmp('LaTeX', 'Latex')
    True
    >>> istrcmp('a', 'b')
    False
```
## Expressões condicionais
​
​
**14):** Qual será a saída dos próximos programas?
​
```
​
    print(2 < 3 and 3 > 1)
    print(2 < 3 or 3 > 1)
    print(2 < 3 or not 3 > 1)
    print(2 < 3 and not 3 > 1)
```
**15):** 
​
```
​
    x = 4
    y = 5
    p = x < y or x < z
    print(p)
```
**16):** 
​
```
​
    True, False = False, True
    print(True, False)
    print(2 < 3)
​
```
**17): ** O que acontece quando os seguinte códigos são executados? Algum erro acontece? explique a razão
​
```
​
    x = 2
    if x == 2:
        print(x)
    else:
        print(y)
```
**18):** 
​
```
​
    x = 2
    if x == 2:
        print(x)
    else:
        x +
```
## Listas e Repeticões

**19):** Qual será a saída do seguinte programa?

```

	x = [0, 1, [2]]
	x[2][0] = 3
	print x
	x[2].append(4)
	print x
	x[2] = 2
	print x

```



