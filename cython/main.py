# import pyximport
# pyximport.install(pyimport = True)
import test
import timeit

def create_grid(n):
    grid = list()
    for i in range(n):
        for j in range(n):
            grid += [(i, j)]
    return grid 

def power(n, power):
    sum = 1
    for i in range(power):
        sum *= n
    return sum    

if __name__ == '__main__':
    # print('PYX:',timeit.timeit('test.create_grid(10)', setup="import test"))
    # print('PY :',timeit.timeit('create_grid(10)', globals=globals()))
    # print('PYX:',timeit.timeit('test.power(2, 100)', setup="import test"))
    # print('PY :',timeit.timeit('power(2, 100)', globals=globals()))
    # print('result :',test.power(2, 100))
    print('PYX:',timeit.timeit('test.primes(100)', setup="import test"))
    print('prime result:',test.primes(100))