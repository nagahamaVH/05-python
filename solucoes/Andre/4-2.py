def fizz_buzz(x):
    if x %3 == 0 and x %5 == 0 :
        return "FizzBuzz"
    elif x %3 == 0: 
        return "Fizz"
    elif x %5 == 0:
        return "Buzz"
    else:
        return x

print(fizz_buzz(15),fizz_buzz(9),fizz_buzz(25),fizz_buzz(11))