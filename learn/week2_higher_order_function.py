'''
    Higer Order Function
'''

is_odd = lambda x: x%2!=0
gen_odd = lambda x: 2*x+1

assert is_odd(3) == True
assert is_odd(6) == False
assert gen_odd(1) == 3
assert gen_odd(3) == 7

if __name__ == '__main__':
    print(is_odd(gen_odd(5)))


