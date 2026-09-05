# factorial of numbers by recursion

num = int(input("Enter any number to get factorial value: "))
def factorial(n):
    if n == 0 or n == 1:
        return 1 
    return n *factorial(n-1) 

print(factorial(num))

# Fibonacci series -  return sum of prev two as nxt number

def fib(n):
    if n == 1 or n ==2 :
        return 1 
    else:
        return fib(n-1) + fib(n-2)