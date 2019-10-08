# python

Referências dos slides e exercícios:

* https://github.com/learnbyexample/Python_Basics
* https://python.swaroopch.com/
* https://www.oreilly.com/programming/free/files/a-whirlwind-tour-of-python.pdf
* https://docs.python-guide.org/
* https://anandology.com/python-practice-book/index.html?utm_source=devfreebooks&utm_medium=medium&utm_campaign=DevFreeBooks
* https://automatetheboringstuff.com/?utm_source=devfreebooks&utm_medium=medium&utm_campaign=DevFreeBooks
* https://penseallen.github.io/PensePython2e/
* https://www.practicepython.org/

# Exemplos

```
chmod +x hello_world.py

$ ./hello_world.py
Hello World
```

# Números

## Inteiros
```
num1 = 7
num2 = 42
total = num1 + num2
```

## float
```
appx_pi = 22 / 7
area = 42.16
appx_pi + area
```

## Notação Científica
```
sci_num1 = 3.982e5
```

## String
```
str1 = 'hello'
str3 = "world"
print(str1 + str3)
```

## Exemplos de operações

* arithmetic operators
    * `+` addition
    * `-` subtraction
    * `*` multiplication
    * `/` division (float output)
    * `//` division (integer output, result is not rounded)
    * `**` exponentiation
    * `%` modulo
* string operators
    * `+` string concatenation
    * `*` string repetition
* comparison operators
    * `==` equal to
    * `>` greater than
    * `<` less than
    * `!=` not equal to
    * `>=` greater than or equal to
    * `<=` less than or equal to
* boolean logic
    * `and` logical and
    * `or` logical or
    * `not` logical not
* bitwise operators
    * `&` and
    * `|` or
    * `^` exclusive or
    * `~` invert bits
    * `>>` right shift
    * `<<` left shift

## def

```
#!/usr/bin/python3

# ----- function without arguments -----
def greeting():
    print("-----------------------------")
    print("         Hello World         ")
    print("-----------------------------")

greeting()
```

## Argumentos

```
# ----- function with arguments -----
def sum_two_numbers(num1, num2):
    total = num1 + num2
    print("{} + {} = {}".format(num1, num2, total))

sum_two_numbers(3, 4)

# ----- function with return value -----
def num_square(num):
    return num * num

my_num = 3
print(num_square(2))
print(num_square(my_num))
```

## Argumento Padrão

```python
#!/usr/bin/python3

# ----- function with default valued argument -----
def greeting(style_char='-'):
    print(style_char * 29)
    print("         Hello World         ")
    print(style_char * 29)

print("Default style")
greeting()

print("\nStyle character *")
greeting('*')

print("\nStyle character =")
greeting(style_char='=')

>>> items = 15
>>> print("No. of items:", items)

```

```python
>>> import sys
>>> print("Error!! Not a valid input", file=sys.stderr)
Error!! Not a valid input
```

## Range

```python
>>> range(5)
range(0, 5)

>>> list(range(5))
[0, 1, 2, 3, 4]

>>> list(range(-2, 2))
[-2, -1, 0, 1]

>>> list(range(1, 15, 2))
[1, 3, 5, 7, 9, 11, 13]

>>> list(range(10, -5, -2))
[10, 8, 6, 4, 2, 0, -2, -4]
```

## type 

```python
>>> type(5)
<class 'int'>

>>> type('Hi there!')
<class 'str'>

>>> type(range(7))
<class 'range'>

>>> type(None)
<class 'NoneType'>

>>> type(True)
<class 'bool'>

>>> arr = list(range(4))
>>> arr
[0, 1, 2, 3]
>>> type(arr)
<class 'list'>
```

## Escopo

```
#!/usr/bin/python3

def print_num():
    print("Yeehaw! num is visible in this scope, its value is: " + str(num))

num = 25
print_num()
```

```
$ ./variable_scope_1.py 
Yeehaw! num is visible in this scope, its value is: 25
```


```python
#!/usr/bin/python3

def square_of_num(num):
    sqr_num = num * num

square_of_num(5)
print("5 * 5 = {}".format(sqr_num))
```

```
$ ./variable_scope_2.py 
Traceback (most recent call last):
  File "./variable_scope_2.py", line 7, in <module>
    print("5 * 5 = {}".format(sqr_num))
NameError: name 'sqr_num' is not defined
```

definindo variável  `global` 

```python
#!/usr/bin/python3

def square_of_num(num):
    global sqr_num
    sqr_num = num * num

square_of_num(5)
print("5 * 5 = {}".format(sqr_num))
```

```
$ ./variable_scope_3.py
5 * 5 = 25
```


```python
#!/usr/bin/python3

sqr_num = 4

def square_of_num(num):
    sqr_num = num * num
    print("5 * 5 = {}".format(sqr_num))

square_of_num(5)
print("Whoops! sqr_num is still {}!".format(sqr_num))
```


```
$ ./variable_scope_4.py 
5 * 5 = 25
Whoops! sqr_num is still 4!
```

## Estruturas de controle

* Combinação de testes

```python
>>> num = 5
>>> num > 2
True
>>> num > 3 and num <= 5
True
>>> 3 < num <= 5
True
>>> num % 3 == 0 or num % 5 == 0
True

>>> fav_fiction = 'Harry Potter'
>>> fav_detective = 'Sherlock Holmes'
>>> fav_fiction == fav_detective
False
>>> fav_fiction == "Harry Potter"
True
```

* Testando variáveis ou valores

```python
>>> bool(num)
True
>>> bool(fav_detective)
True
>>> bool(3)
True
>>> bool(0)
False
>>> bool("")
False
>>> bool(None)
False

```

* operador `in` 

```python
>>> def num_chk(n):
...     if n == 10 or n == 21 or n == 33:
...         print("Number passes condition")
...     else:
...         print("Number fails condition")
... 
>>> num_chk(10)
Number passes condition
>>> num_chk(12)
Number fails condition
```

* operador `in` 

```python
>>> def num_chk(n):
...     if n in (10, 21, 33):
...         print("Number passes condition")
...     else:
...         print("Number fails condition")
... 
>>> num_chk(12)
Number fails condition
>>> num_chk(10)
Number passes condition
```


## if

```python
#!/usr/bin/python3

num = 45

# only if
if num > 25:
    print("Hurray! {} is greater than 25".format(num))

# if-else
if num % 2 == 0:
    print("{} is an even number".format(num))
else:
    print("{} is an odd number".format(num))

# if-elif-else
# any number of elif can be used
if num < 0:
    print("{} is a negative number".format(num))
elif num > 0:
    print("{} is a positive number".format(num))
else:
    print("{} is neither postive nor a negative number".format(num))
```


```
$ ./if_elif_else.py 
Hurray! 45 is greater than 25
45 is an odd number
45 is a positive number
```

**if-else** 

```python
#!/usr/bin/python3

num = 42

num_type = 'even' if num % 2 == 0 else 'odd'
print("{} is an {} number".format(num, num_type))
```


```
$ ./if_else_oneliner.py 
42 is an even number
```

## for

```python
#!/usr/bin/python3

number = 9
for i in range(1, 5):
    mul_table = number * i
    print("{} * {} = {}".format(number, i, mul_table))
```

while

```python
#!/usr/bin/python3

# continuously ask user input till it is a positive integer
usr_string = 'not a number'
while not usr_string.isnumeric():
    usr_string = input("Enter a positive integer: ")
```


```
$ ./while_loop.py 
Enter a positive integer: abc
Enter a positive integer: 1.2
Enter a positive integer: 23
$ 
```


**continue** - pule o restante das instruções no loop (se houver) e o loop de saída

```python
#!/usr/bin/python3

prev_num = 0
curr_num = 0
print("The first ten numbers in fibonacci sequence: ", end='')

for num in range(10):
    print(curr_num, end=' ')

    if num == 0:
        curr_num = 1
        continue

    temp = curr_num
    curr_num = curr_num + prev_num
    prev_num = temp

print("")
```

```
$ ./loop_with_continue.py 
The first ten numbers in fibonacci sequence: 0 1 1 2 3 5 8 13 21 34
```

**break** - pule o restante das instruções no loop (se houver) e sai do loop

```python
#!/usr/bin/python3

import random

while True:
    # as with range() function, 500 is not inclusive
    random_int = random.randrange(500)
    if random_int % 4 == 0 and random_int % 6 == 0:
        break
print("Random number divisible by 4 and 6: {}".format(random_int))
```

## while 

```
$ ./loop_with_break.py 
Random number divisible by 4 and 6: 168
$ ./loop_with_break.py 
Random number divisible by 4 and 6: 216
$ ./loop_with_break.py 
Random number divisible by 4 and 6: 24
```

## while e break

```python
>>> while True:
         usr_string = input("Enter a positive integer: ")
         if usr_string.isnumeric():
             break
    
Enter a positive integer: a
Enter a positive integer: 3.14
Enter a positive integer: 1
>>>
```

