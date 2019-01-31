'''
	Multiples of 3 and 5

    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
'''
from functools import reduce

is_divide_by3 = lambda x: x%3==0
is_divide_by5 = lambda x: x%5==0

assert is_divide_by3(6) == True
assert is_divide_by3(11) == False
assert is_divide_by5(4) == False
assert is_divide_by5(10) == True

def gen_natural_number(start=3, end=1000):
    for i in range(start, end):
        if is_divide_by3(i) or is_divide_by5(i):
            yield i

natural_number = list(gen_natural_number())
print(natural_number)

summation = lambda x, y: x+y
sum_ = reduce(summation, natural_number)
print(sum_)