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
    open_text = open("./solaces/data/she.txt", "r")
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
