'''
    Generating Function
    :yield <-- return
'''

def gen_even(start=0, end=10):
    for i in range(start, end+1):
        yield 2*i

if __name__ == '__main__':
    # print(list(gen_even(100000, 200000)))
    # for i in gen_even():
    #     print(i)

    evens = gen_even(0, 100000000000000000000)    
    print(next(evens))
    print(next(evens))
    print(next(evens))
    print(next(evens))
    print(next(evens))