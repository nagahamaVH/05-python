def factorial(x):
    if x < 0:
        raise ValueError

    prod = 1
    for i in range(1, (x + 1)):
        prod *= i
    return prod
