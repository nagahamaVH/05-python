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
