
def f(x):
    return x**2

'''
    lambda (var1, var2, var3): <exp>
    short-hand if else 
    lambda x: x if x > 10 else 0
'''

g = lambda x: x**2
is_even = lambda x: True if x%2==0 else False
is_even2 = lambda x: x%2==0 

if __name__ == '__main__':
    assert is_even2(4) == True
    assert is_even2(7) == False

    print('f(2)=', f(2))
    print('g(2)=', g(2))
    print('2 is even ', is_even(2))
    print('2 is even ', is_even2(2))
    print('5 is even ', is_even2(5))