'''
    Maps, Reduce and Filter
'''

data = [1,2,3,4,5]

#! MAPS
pow2 = lambda x: x*x
modified_data = map(pow2, data)
print(list(modified_data))

md2 = map(lambda x:x+100, data)
print(list(md2))

# Comprehensive list 
md3 = [x for x in map(lambda x:x+100, data)]
print(md3)

#* RECOMMEND Best practice
md4 = [x for x in map(pow2, data)]
print(md4)

# Lambda Style
ml_data = ['abc', 'abb', 'acc']
cut_a = lambda x: x.replace('a','')
new_data = [x for x in map(cut_a, ml_data)]
print(new_data)

#Looping Style
result = []
for x in ml_data:
    k = cut_a(x)
    result.append(k)
print(result)    

#! REDUCE
from functools import reduce

summation = lambda x, y : x+y
sum_ = reduce(summation, data)
print(sum_)

products = lambda x, y : x*y 
prod_ = reduce(products, data)
print(prod_)

#! FILTER
is_even = lambda x: x%2==0
even_data = filter(is_even, data)
print(list(even_data))

is_odd = lambda x: not is_even(x)
odd_data = [ x for x in filter(is_odd, data)]   
print(odd_data)

word = ['abc', 'a', 'xyz', 'abcdefg' , 'qaz']
only_abc = lambda x: x in 'abc'
print(list(filter(only_abc, word)))

