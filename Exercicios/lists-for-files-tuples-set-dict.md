
# Working with Data


## Lists

**problem 1:** What will be the output of the following program?

```

	x = [0, 1, [2]]
	x[2][0] = 3
	print x
	x[2].append(4)
	print x
	x[2] = 2
	print x

```
### The for Statement

**problem 2:** Python has a built-in function ``sum`` to find sum of all elements of a list. Provide an implementation for ``sum``. 

```

    >>> sum([1, 2, 3])
    >>> 6
```
**problem 3:** What happens when the above ``sum`` function is called with a list of strings? Can you make your ``sum`` function work for a list of strings as well.

```

    >>> sum(["hello", "world"])
    "helloworld"
    >>> sum(["aa", "bb", "cc"])
    "aabbcc"
```
**problem 4:** Implement a function ``product``, to compute product of a list of numbers.

```

    >>> product([1, 2, 3])
    6
```
**problem 5:** Write a function ``factorial`` to compute factorial of a number.
   Can you use the ``product`` function defined in the previous example to
   compute factorial?

```

    >>> factorial(4)
    24
```
**problem 6:** Write a function ``reverse`` to reverse a list. Can you do this
   without using list slicing?

```

    >>> reverse([1, 2, 3, 4])
    [4, 3, 2, 1]
    >>> reverse(reverse([1, 2, 3, 4]))
    [1, 2, 3, 4]
```
**problem 7:** Python has built-in functions ``min`` and ``max`` to compute
   minimum and maximum of a given list. Provide an implementation for these
   functions. What happens when you call your ``min`` and ``max`` functions with a
   list of strings? 

**problem 8:** Cumulative sum of a list ``[a, b, c, ...]`` is defined as ``[a,
   a+b, a+b+c, ...]``. Write a function ``cumulative_sum`` to compute
   cumulative sum of a list. Does your implementation work for a list of strings?

```

    >>> cumulative_sum([1, 2, 3, 4])
    [1, 3, 6, 10]
    >>> cumulative_sum([4, 3, 2, 1])
    [4, 7, 9, 10]
```
**problem 9:** Write a function ``cumulative_product`` to compute cumulative
   product of a list of numbers.

```

    >>> cumulative_product([1, 2, 3, 4])
    [1, 2, 6, 24]
    >>> cumulative_product([4, 3, 2, 1])
    [4, 12, 24, 24]
```
**problem 10:** Write a function `unique` to find all the unique elements of a list.

```

	>>> unique([1, 2, 1, 3, 2, 5])
	[1, 2, 3, 5]
```    
**problem 11:** Write a function `dups` to find all duplicates in the list.

```

	>>> dups([1, 2, 1, 3, 2, 5])
	[1, 2]
```
**problem 12:** Write a function `group(list, size)` that take a list and splits
   into smaller lists of given size.

```

    >>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 3)
    [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    >>> group([1, 2, 3, 4, 5, 6, 7, 8, 9], 4)
    [[1, 2, 3, 4], [5, 6, 7, 8], [9]]    
```
## Sorting Lists

**problem 14:** Write a function ``lensort`` to sort a list of strings based on length.

```

    >>> lensort(['python', 'perl', 'java', 'c', 'haskell', 'ruby'])
    ['c', 'perl', 'java', 'ruby', 'python', 'haskell']

```
**problem 15:** Improve the `unique` function written in previous problems to take
   an optional `key` function as argument and use the return value of the key
   function to check for uniqueness.

```

	>>> unique(["python", "java", "Python", "Java"], key=lambda s: s.lower())
	["python", "java"]
```
## Tuples

**problem 16:** Reimplement the `unique` function implemented in the earlier
   examples using sets. 
    
## Strings
    
**problem 17:** Write a function ``extsort`` to sort a list of files based on extension. 

```

    >>> extsort(['a.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt', 'x.c'])
    ['a.c', 'x.c', 'a.py', 'b.py', 'bar.txt', 'foo.txt']
```    
## Working With Files

**problem 18:** Write a program ``reverse.py`` to print lines of a file in reverse order.

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
**problem 19:** Write a program to print each line of a file in reverse order.

**problem 20:** Implement unix commands ``head`` and ``tail``. The ``head`` and ``tail`` commands take a file as argument and prints its first and last 10 lines of the file respectively.

**problem 21:** Implement unix command ``grep``. The ``grep`` command takes a string and a file as arguments and prints all lines in the file which contain the specified string.

```
    $ python grep.py she.txt sure
    The shells that she sells are seashells I'm sure.
    I'm sure that the shells are seashore shells.
```
**problem 22:** Write a program `wrap.py` that takes filename and width as aruguments and wraps the lines longer than `width`.

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
**problem 23:** The above wrap program is not so nice because it is breaking the line at middle of any word. Can you write a new program `wordwrap.py` that works like `wrap.py`, but breaks the line only at the word boundaries?

```
    $ python wordwrap.py she.txt 30
    I'm sure that the shells are
    seashore shells.
    So if she sells seashells on
    the seashore,
    The shells that she sells are
    seashells I'm sure.
    She sells seashells on the
    seashore;
```
**problem 24:** Write a program `center_align.py` to center align all lines in the given file.

```
    $ python center_align.py she.txt
      I'm sure that the shells are seashore shells.  
        So if she sells seashells on the seashore,   
    The shells that she sells are seashells I'm sure.
           She sells seashells on the seashore;      
```    
## List Comprehensions

**problem 25:** Provide an implementation for ``zip`` function using list comprehensions.

```

    >>> zip([1, 2, 3], ["a", "b", "c"])
    [(1, "a"), (2, "b"), (3, "c")]
```
**problem 26:** Python provides a built-in function ``map`` that applies a function to each element of a list. Provide an implementation for ``map`` using list comprehensions.

```

    >>> def square(x): return x * x
    ...
    >>> map(square, range(5))
    [0, 1, 4, 9, 16]
```
**problem 27:** Python provides a built-in function ``filter(f, a)`` that returns items of the list ``a`` for which ``f(item)`` returns true. Provide an implementation for ``filter`` using list comprehensions.

```

    >>> def even(x): return x %2 == 0
    ...
    >>> filter(even, range(10))
    [0, 2, 4, 6, 8]
```  
**problem 28:** Write a function ``triplets`` that takes a number ``n`` as argument and returns a list of triplets such that sum of first two elements of the triplet equals the third element using numbers below n. Please note that ``(a, b, c)`` and ``(b, a, c)`` represent same triplet.

```

    >>> triplets(5)
    [(1, 1, 2), (1, 2, 3), (1, 3, 4), (2, 2, 4)]
```
**problem 29:** Write a function ``enumerate`` that takes a list and returns a list of tuples containing ``(index,item)`` for each item in the list.

```

    >>> enumerate(["a", "b", "c"])
    [(0, "a"), (1, "b"), (2, "c")]
    >>> for index, value in enumerate(["a", "b", "c"]):
    ...     print index, value
    0 a
    1 b
    2 c
```
**problem 30:** Write a function ``array`` to create an 2-dimensional array. The function should take both dimensions as arguments. Value of each element can be initialized to None:

```

    >>> a = array(2, 3)
    >>> a
    [[None, None, None], [None, None, None]]
    >>> a[0][0] = 5
    [[5, None, None], [None, None, None]]
```
**problem 31:** Write a python function ``parse_csv`` to parse csv (comma separated values) files.

```

    >>> print open('a.csv').read()
    a,b,c
    1,2,3
    2,3,4
    3,4,5
    >>> parse_csv('a.csv')
    [['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]
```
**problem 32:** Generalize the above implementation of csv parser to support any delimiter and comments.

```

    >>> print open('a.txt').read()
    # elements are separated by ! and comment indicator is #
    a!b!c
    1!2!3
    2!3!4
    3!4!5
    >>> parse('a.txt', '!', '#')
    [['a', 'b', 'c'], ['1', '2', '3'], ['2', '3', '4'], ['3', '4', '5']]
```
**problem 33:** Write a function ``mutate`` to compute all words generated by a single mutation on a given word. A mutation is defined as inserting a character, deleting a character, replacing a character, or swapping 2 consecutive characters in a string. For simplicity consider only letters from ``a`` to ``z``.

```

    >>> words = mutate('hello')
    >>> 'helo' in words
    True
    >>> 'cello' in words
    True
    >>> 'helol' in words
    True
 ```
**problem 34:** Write a function ``nearly_equal`` to test whether two strings are nearly equal. Two strings ``a`` and ``b`` are nearly equal when ``a`` can be generated by a single mutation on ``b``.

```

    >>> nearly_equal('python', 'perl')
    False
    >>> nearly_equal('perl', 'pearl')
    True
    >>> nearly_equal('python', 'jython')
    True
    >>> nearly_equal('man', 'woman')
    False
```
## Dictionaries

**problem 36:** Write a program to count frequency of characters in a given file. Can you use character frequency to tell whether the given file is a Python program file, C program file or a text file?

**problem 37:** Write a program to find anagrams in a given list of words. Two words are called anagrams if one word can be formed by rearranging letters of another. For example 'eat', 'ate' and 'tea' are anagrams. 

```

    >>> anagrams(['eat', 'ate', 'done', 'tea', 'soup', 'node'])
    [['eat', 'ate', 'tea], ['done', 'node'], ['soup']]
```    
**problem 38:** Write a function ``valuesort`` to sort values of a dictionary based on the key.

```

    >>> valuesort({'x': 1, 'y': 2, 'a': 3})
    [3, 1, 2]
```
**problem 39:** Write a function ``invertdict`` to interchange keys and values in a dictionary. For simplicity, assume that all values are unique.

```

    >>> invertdict({'x': 1, 'y': 2, 'z': 3})
    {1: 'x', 2: 'y', 3: 'z'}
```
