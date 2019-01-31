'''
    Even Fibonacci numbers

    Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

                1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''
from functools import reduce

is_even = lambda x: x%2==0

def gen_fibonacci(var1, var2):
    if var2 >=1:
        yield 1
    else:
        yield gen_fibonacci(var1, var2) 

# fibo_number = gen_fibonacci(1, 2) 
# print(fibo_number) 