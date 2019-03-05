def id2(double exceed):
    
    cdef double a=1, b=1, temp=1, sum=0
    while b < exceed:
        temp = b
        b = a+b
        a = temp
        if is_even(temp):
            sum+=temp
    return sum    

def is_even(double a):
    return a%2==0
