#Docstrings
def square(n):
    '''Takes in a number n,gives square of n'''
    print(n**2)
square(5)
print(square.__doc__)

#Recursion
#caling a function inside a function
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(5))

#Fibonaci Sequence
def f(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return f(n-1)+f(n-2)
    
print(f(7))
