## Listas

### Listas Simples

```python
vowels = ['a', 'e', 'i', 'o', 'u']
vowels
vowels[0]
vowels[10]

>>> even_numbers = list(range(2, 11, 2))
>>> even_numbers
[2, 4, 6, 8, 10]
>>> even_numbers[-1]

>>> even_numbers[-2]

>>> even_numbers[-15]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range
```

* Listas multidimensionais e heterogêneas

```python
list_2D = [[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
list_2D[0][0]
list_2D[1][0]
```


### Slice


```python
>>> books = ['Harry Potter', 'Sherlock Holmes', 'To Kill a Mocking Bird']
>>> books[2] = "Ender's Game"
>>> print(books)
['Harry Potter', 'Sherlock Holmes', "Ender's Game"]

>>> prime = [2, 3, 5, 7, 11]
>>> prime[2:4]
>>> prime[:3]
>>> prime[3:]

>>> prime[-1]
>>> prime[-1:]
>>> prime[-2:]

>>> prime[::1]
>>> prime[::2]
>>> prime[3:1:-1]
>>> prime[::-1]
>>> prime[:]
```


```python
>>> nums = [1.2, -0.2, 0, 2]
>>> nums[:2] = [1]
>>> nums

>>> nums = [1.2, -0.2, 0, 2, 4, 23]
>>> nums[:5:2] = [1, 4, 3]
>>> nums

>>> nums = [1, 2, 3, 23]
>>> nums[::-1] = [1, 4, 5, 2]
>>> nums
```

* associação sem modificar id

```python
>>> id(nums)
>>> nums[:] = [1, 2, 5, 4.3]
>>> nums
[1, 2, 5, 4.3]
>>> id(nums)


# associação sem  [:] trocar o id
>>> nums = [1.2, -0.2, 0, 2]
>>> id(nums)
140598782943752
```

## copiando listas

```python
>>> a = 10

>>> b = a
>>> id(b)
>>> b = 4
>>> b
>>> a
```

* Para ementos mutáveis como listas os valores se alteram ao ser copiados

```python
>>> a = [1, 2, 5, 4.3]
>>> a

>>> b = a
>>> b

>>> id(a)
>>> id(b)

>>> b[0] = 'xyz'
>>> b
>>> a
```

* Funciona pra 1D mas pode falhar em múltiplas dimensões

```python
>>> prime = [2, 3, 5, 7, 11]
>>> b = prime[:]
>>> id(prime)
140684818101064
>>> id(b)
140684818886024
>>> b[0] = 'a'
>>> b
['a', 3, 5, 7, 11]
>>> prime
[2, 3, 5, 7, 11]

>>> list_2D = [[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> a = list_2D[:]
>>> id(list_2D)
140684818102344
>>> id(a)
140684818103048
>>> a
[[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> a[0][0] = 'a'
>>> a
[['a', 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> list_2D
[['a', 3, 2, 10], [1.2, -0.2, 0, 2]]
```

* Módulo de cópia

```python
>>> import copy
>>> list_2D = [[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> c = copy.deepcopy(list_2D)
>>> c[0][0] = 'a'
>>> c
[['a', 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> list_2D
[[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
```


* adicionando elementos a uma lista

```python
>>> books = []
>>> books
[]
>>> books.append('Harry Potter')
>>> books
['Harry Potter']

>>> even_numbers
[2, 4, 6, 8, 10]
>>> even_numbers += [12, 14, 16, 18, 20]
>>> even_numbers
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

>>> even_numbers = [2, 4, 6, 8, 10]
>>> even_numbers.extend([12, 14, 16, 18, 20])
>>> even_numbers
[2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

>>> a = [[1, 3], [2, 4]]
>>> a.extend([[5, 6]])
>>> a
[[1, 3], [2, 4], [5, 6]]
```

* Apagando elementos

```python
>>> prime = [2, 3, 5, 7, 11]
>>> prime.pop()
11
>>> prime
[2, 3, 5, 7]
>>> prime.pop(0)
2
>>> prime
[3, 5, 7]

>>> list_2D = [[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> list_2D[0].pop(0)
1
>>> list_2D
[[3, 2, 10], [1.2, -0.2, 0, 2]]

>>> list_2D.pop(1)
[1.2, -0.2, 0, 2]
>>> list_2D
[[3, 2, 10]]
```



```python
>>> nums = [1.2, -0.2, 0, 2, 4, 23]
>>> del nums[1]
>>> nums
[1.2, 0, 2, 4, 23]

# slicing

>>> del nums[1:4]
>>> nums
[1.2, 23]

>>> list_2D = [[1, 3, 2, 10], [1.2, -0.2, 0, 2]]
>>> del list_2D[0][1]
>>> list_2D
[[1, 2, 10], [1.2, -0.2, 0, 2]]

>>> del list_2D[0]
>>> list_2D
[[1.2, -0.2, 0, 2]]
```

* limpando uma lista

```python
>>> prime = [2, 3, 5, 7, 11]
>>> prime.clear()
>>> prime
[]
```

* apagando com base em um valor
 
```python
>>> even_numbers = [2, 4, 6, 8, 10]
>>> even_numbers.remove(8)
>>> even_numbers
[2, 4, 6, 10]
>>> even_numbers.remove(12)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: list.remove(x): x not in list
```

* inserindo com base em índice

```python
>>> books = ['Harry Potter', 'Sherlock Holmes', 'To Kill a Mocking Bird']
>>> books.insert(2, "The Martian")
>>> books
['Harry Potter', 'Sherlock Holmes', 'The Martian', 'To Kill a Mocking Bird']
```

* obtendo índice do elemento

```python
>>> even_numbers = [2, 4, 6, 8, 10]
>>> even_numbers.index(6)
2
>>> even_numbers.index(12)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: 12 is not in list
```

* operador in para verificar se existe um elemento

```python
>>> prime = [2, 3, 5, 7, 11]
>>> 3 in prime
True
>>> 13 in prime
False
```

* sort

```python
>>> a = [1, 5.3, 321, 0, 1, 2]
>>> a.sort()
>>> a
[0, 1, 1, 2, 5.3, 321]

>>> a = [1, 5.3, 321, 0, 1, 2]
>>> a.sort(reverse=True)
>>> a
[321, 5.3, 2, 1, 1, 0]
```

* Sort

```python
>>> words = ['fuliginous', 'crusado', 'morello', 'irk', 'seam']
>>> words.sort(key=len)
>>> words
['irk', 'seam', 'crusado', 'morello', 'fuliginous']

>>> words.sort(key=lambda x: x[1])
>>> words
['seam', 'morello', 'irk', 'crusado', 'fuliginous']
```

If original list should not be changed, use [sorted](https://docs.python.org/3/library/functions.html#sorted) function

```python
>>> nums = [-1, 34, 0.2, -4, 309]
>>> nums_desc = sorted(nums, reverse=True)
>>> nums_desc
[309, 34, 0.2, -1, -4]

>>> sorted(nums, key=abs)
[0.2, -1, -4, 34, 309]
```

* `min`  `max`

```python
>>> a = [321, 899.232, 5.3, 2, 1, -1]
>>> min(a)
-1
>>> max(a)
899.232
```

* contando itens

```python
>>> nums = [15, 99, 19, 382, 43, 19]
>>> nums.count(99)
1
>>> nums.count(19)
2
>>> nums.count(23)
0
```

* lista reversa

```python
>>> prime = [2, 3, 5, 7, 11]
>>> id(prime)
140684818102088
>>> prime.reverse()
>>> prime
[11, 7, 5, 3, 2]
>>> id(prime)
140684818102088

>>> a = [1, 5.3, 321, 0, 1, 2]
>>> id(a)
140684818886024
>>> a = a[::-1]
>>> a
[2, 1, 0, 321, 5.3, 1]
>>> id(a)
140684818102664
```

* len

```python
>>> prime
[2, 3, 5, 7, 11]
>>> len(prime)
5

>>> s = len(prime) // 2
>>> prime[:s]
[2, 3]
>>> prime[s:]
[5, 7, 11]
```

* somando

```python
>>> a
[321, 5.3, 2, 1, 1, 0]
>>> sum(a)
330.3
```

* all

```python
>>> conditions = [True, False, True]
>>> all(conditions)
False
>>> any(conditions)
True

>>> conditions[1] = True
>>> all(conditions)
True

>>> a = [321, 5.3, 2, 1, 1, 0]
>>> all(a)
False
>>> any(a)
True
```

* comparação

```python
>>> prime
[2, 3, 5, 7, 11]
>>> a = [4, 2]
>>> prime == a
False

>>> prime == [2, 3, 5, 11, 7]
False
>>> prime == [2, 3, 5, 7, 11]
True
```

* list comprehension

```python
# using if-else conditional in list comprehension
numbers = [2, 12, 3, 25, 624, 21, 5, 9, 12]
odd_numbers  = []
even_numbers = []
[odd_numbers.append(num) if(num % 2) else even_numbers.append(num) for num in numbers]

# or a more simpler and readable approach
numbers = [2, 12, 3, 25, 624, 21, 5, 9, 12]
odd_numbers  = [num for num in numbers if num % 2]
even_numbers = [num for num in numbers if not num % 2]
```

* Obtendo item aleatório

```python
>>> import random
>>> a = [4, 5, 2, 76]
>>> random.choice(a)
76
>>> random.choice(a)
4
```

