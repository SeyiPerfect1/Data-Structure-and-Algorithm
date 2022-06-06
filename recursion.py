# iterative solution of factorial


def fact(n):
    fac_sum = 1
    if n > 0:
        for i in range(n, 0, -1):
           fac_sum *= i
        return fac_sum
    elif n == 0:
        return 1
    else:
        print('Invalid Number!!!')

#Recusive solution of factorial
def recusivefact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*recusivefact(n-1)

        

#iterative solution of fibonacci
def fib(n):
    fib1 = 0
    fib2 = 1
    if n < 0:
        print("invalid number")
    
    elif n == 0:
        return fib1
    
    elif n == 1:
        return fib2

    else:
        for i in range(2, n+1):
            sum = fib1 + fib2
            fib1 = fib2
            fib2 = sum
        return sum


#Test
if __name__ =="__main__":
    n = 9
    fib(n)
    
        
#recursive solution of fibonaci
def recursivefib(n):
    if n==1 or n==0:
        return 1
    else:
        return recursivefib(n-1)+recursivefib(n-2)

        
    




        





    
     
