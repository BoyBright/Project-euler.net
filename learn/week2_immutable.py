'''
    Immuable State 
    all id is the same that mean 'address' is same
    that why int, bool, float, str, tuple, frozenset is Immutable
    cuz It can't change
'''

if __name__ == '__main__':
    x = 5
    y = x
    print('id(5)',id(5))
    print('id(x)',id(x))
    print('id(y)',id(y))