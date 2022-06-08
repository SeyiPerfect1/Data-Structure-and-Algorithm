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


#test 
if __name__ == "__main__":
    fact(7)
    fact(-1)
    fact(20)
    fact(0)



#Recusive solution of factorial
def recusiveFact(n):
    if n < 0:
        print('invalid number')

    elif n == 0 or n == 1:
        return 1

    else:
        return n*recusiveFact(n-1)


#test 
if __name__ == "__main__":
    recusiveFact(7)
    recusiveFact(-1)
    recusiveFact(20)
    recusiveFact(0)



        

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
    fib(9)
    fib(-1)
    fib(0)

    
        
#recursive solution of fibonaci
def recursivefib(n):
    if n==1:
        return 1

    elif n>1:
        return recursivefib(n-1)+recursivefib(n-2)

    else:
        print("invalid number")


#Test
if __name__ =="__main__":
    recursivefib(9)
    recursivefib(-1)
    recursivefib(0)


#improved code for fibonacci series using Dynamic Programming
def fib(n):
    a = [0, 1]

    for i in range(2, n+1):
        a.append(a[i-1] + a[i-2])

    return[a[n]]


#driver/test code
if __name__ =="__main__":

    print(fib(9))
    print(fib(-1))




#exponential for positive integers
#n is the number
#m is the exp
def exp(n, m):
    if m == 0:
        return 1

    elif m==1:
        return n

    else:
        mul = n
        for i in range(1,m):
            mul *= n
        return mul


#test
if __name__ == "__main__":
    exp(2, 0)
    exp(3, 5)
    exp(2, 3)
    exp(3, 8)



#exponential using recursive method
def exp(n, m):
    if m==0:
        return 1

    else:
        return n * exp(n, m-1)

#test
if __name__ == "__main__":
    exp(2, 0)
    exp(3, 5)
    exp(2, 3)
    exp(3, 8)


#improved code
def exp(n, m):
    if m==0:
        return 1

    elif m%2==1:
        return n * exp(n, m-1)

    elif m%2==0:
        y = exp(n, m/2)
        return y*y 

#test
if __name__ == "__main__":
    exp(2, 0)
    exp(3, 5)
    exp(2, 3)
    exp(3, 8)





        
    




        





    
     
