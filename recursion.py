# iterative recursion approach
def fact(n):
    facsum = 1
    if n > 0:
        for i in range(n, 0, -1):
           facsum *= i
        return facsum
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
    fibList = [0]
    while True:
        if n<=1:
            return 1

        elif fib2>=n:
            break
        sum = fib1 + fib2
        fibList.append(sum)
        fib1 = fib2
        fib2 = sum
    return fibList
        
#recursive solution of fibonaci
def recursivefib(n):
    if n <=1:
        return 1
    else:
        return recursivefib(n-1)+fib(n-2)

        
    




        





    
     
