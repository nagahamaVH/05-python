# Arquivos

## open

## Read

```
filename = 'hello_world.py'
f = open(filename, 'r', encoding='ascii')

print("conteúdo " + filename)
print('-' * 30)
for line in f:
    print(line, end='')

f.close()

# usando 'with'
filename = 'while_loop.py'

print("\n\n conteúdo " + filename)
print('-' * 30)
with open(filename, 'r', encoding='ascii') as f:
    for line in f:
        print(line, end='')
```


* arquivo nao existe

```
with open('xyz.py', 'r', encoding='ascii') as f:
    for line in f:
        print(line, end='')
```

* ler todo conteúdo para uma string

```python
>>> f = open('hello_world.py', 'r', encoding='ascii')
>>> f
<_io.TextIOWrapper name='hello_world.py' mode='r' encoding='ascii'>
>>> print(f.read())

```

* linha por linha usando `readline()`

```python
>>> f = open('hello_world.py', 'r', encoding='ascii')
>>> print(f.readline(), end='')
>>> print(f.readline(), end='')
>>> print(f.readline(), end='')

>>> f.close()
>>> print(f.readline(), end='')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ValueError: I/O operation on closed file.
```

* lendo todas as linhas com `readlines()`

```python
>>> f = open('hello_world.py', 'r', encoding='ascii')
>>> all_lines = f.readlines()
>>> all_lines
['#!/usr/bin/python3\n', '\n', 'print("Hello World")\n']
```

* verificar se arquivo fechado

```python
>>> f = open('hello_world.py', 'r', encoding='ascii')

>>> f.closed
False

>>> f.close()
>>> f.closed
True
```

## escrever arquivos

```

with open('new_file.txt', 'w', encoding='ascii') as f:
    f.write("linha 1\n")
    f.write("linha 1\n")
```

```
$ ./file_writing.py
$ cat new_file.txt 
This is a sample line of text
Yet another line
```

## editando com  fileinput

```python
import fileinput

with fileinput.input(inplace=True) as f:
    for line in f:
        line = line.replace('line of text', 'line')
        print(line, end='')
```

```bash
$ ./inplace_file_editing.py new_file.txt
$ cat new_file.txt 
