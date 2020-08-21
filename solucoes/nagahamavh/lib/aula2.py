# Exercicio 15
def factorial(x):
    if x < 0:
        raise ValueError

    prod = 1
    for i in range(1, (x + 1)):
        prod *= i
    return prod


# Exercicio 5
def _sqrt_pow2(x):
    if x < 0:
        result = x ** 2
    else:
        result = x ** (1/2)

    return result


def sqrt_pow2():
    x = input("Digite o valor: ")
    x = float(x)
    result = _sqrt_pow2(x)

    return result


# Exercicio 16
def read_raw(path):
    open_text = open(path, "r")
    text = open_text.read()
    open_text.close()

    return text


def _reverse(text):
    text = text.split("\n")
    text.reverse()
    return text


def reverse(path):
    text = read_raw(path)
    reverse_text = _reverse(text)

    for x in reverse_text:
        print(x)


# Exercicio 19
def get_anagrams(words):
    base = find_base_words(words)
    anagrams = group_anagrams(words, base)

    return anagrams


def find_base_words(words):
    if not isinstance(words, list):
        raise TypeError("The input words must be a list")

    if any(isinstance(w, list) for w in words):
        raise ValueError("List of lists is not allowed")

    base_words = []

    for w in words:
        base_w = "".join(sorted(w))
        base_words.append(base_w)

    return base_words


def group_anagrams(words, base_words):
    if len(words) != len(base_words):
        raise ValueError("Mismatch of input lengths")

    if words == []:
        anagrams = [[]]
    else:
        anagrams = []

        group_words = sorted(set(base_words))

        for gw in group_words:
            subgroup = []
            for i in range(len(base_words)):
                if base_words[i] == gw:
                    subgroup.append(words[i])
            anagrams.append(subgroup)

    return anagrams
