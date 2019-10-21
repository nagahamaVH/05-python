def e_primo(num):

    # If given number is greater than 1 
    if num > 1:

        # Iterate from 2 to n / 2  
        for i in range(2, int(num/2)):

            # If num is divisible by any number between  
            # 2 and n / 2, it is not prime  
            if (num % i) == 0: 
                return False
        else: 
            return True 

    else: 
        return False

def imprime_primos(limite):
    for i in range(limite):
        if e_primo(i):
            print(i)

imprime_primos(100)